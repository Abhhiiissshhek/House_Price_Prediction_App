
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def generate_house_data(n_samples=100):
    np.random.seed(69)

    size = np.random.normal(1400, 50, n_samples)

    # Price = size * 65 + some random noise
    price = size * 65 + np.random.normal(0, 50, n_samples)

    return pd.DataFrame({
        'size': size,
        'price': price
    })


def train_model():

    df = generate_house_data(n_samples=100)

    X = df[['size']]
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def main():

    st.title("Simple Linear Regression House Prediction App")

    st.write("Put in your house size to know its price.")

    model = train_model()

    size = st.number_input(
        'House size',
        min_value=500,
        max_value=2000,
        value=1500
    )

    if st.button('Predict price'):

        input_data = pd.DataFrame({
            'size': [size]
        })

        predicted_price = model.predict(input_data)

        st.success(
            f'Estimated price: ${predicted_price[0]:,.2f}'
        )

        # Generate data for visualization
        df = generate_house_data()

        fig = px.scatter(
            df,
            x="size",
            y="price",
            title="Size vs House Price"
        )

        # Add predicted point
        fig.add_scatter(
            x=[size],
            y=[predicted_price[0]],
            mode='markers',
            marker=dict(
                size=15,
                color='red'
            ),
            name='Prediction'
        )

        st.plotly_chart(fig)


if __name__ == '__main__':
    main()
