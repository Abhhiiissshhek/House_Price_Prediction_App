# House Price Prediction App

A machine learning project that predicts house prices based on features such as area, bedrooms, bathrooms, location, age, and other property characteristics.

The dataset used in this project is **synthetically generated** for learning and experimentation.

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib / Seaborn
* Streamlit
* Joblib

## Dataset

The dataset is created synthetically rather than collected from real-world house listings.
We will soon update this project with real data (asap)

The target variable is:

* **House Price**


## Streamlit App

The trained model is integrated into a Streamlit web application.

Users can enter the house Area and receive an estimated house price.


## Run Locally

Clone the repository:

```bash
git clone <your-repository-url>
cd house-price-prediction
```

Create virtual environment:

```bash
python -m venv venv
.\venv\scripts\activate
```


Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## Live link 
[House_Price_Prediction.app](https://housepricepredictionapp-7ffaeapvqkgw88yqqkappy6.streamlit.app/)


## Disclaimer

This project uses a **synthetic dataset** and is intended for educational purposes. The predictions should not be considered real-world property valuations.

## Future Improvements

* Improve synthetic data generation
* Add more realistic features
* Experiment with additional ML models
* Add feature importance visualization
* Improve the Streamlit UI
* Add model monitoring
* Deploy the application
