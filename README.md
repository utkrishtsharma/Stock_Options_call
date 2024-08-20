# Stock Options Call/Put Prediction App
LIVE APP : https://stockoptionscall-gwnvs2j3tlyecwhx4thjvt.streamlit.app/

## Overview

This is a Streamlit web application that provides live stock market data and predicts whether a "Call" or "Put" option is more likely based on quantitative analysis. The app fetches real-time intraday stock prices for a selected stock symbol and uses a simple machine learning model to suggest options trades.

## Features

- **Live Stock Data:** Fetches and displays real-time intraday stock data for selected stocks.
- **Call/Put Prediction:** Predicts the likelihood of a "Call" or "Put" option based on price trends.
- **Interactive Charts:** Visualizes stock price movements with dynamic charts.
- **Custom Search:** Allows users to search for any stock symbol in addition to predefined options.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/utkrishtsharma/Stock_Options_call.git
   cd Stock_Options_call

Install the Required Packages

Ensure you have Python 3.8+ installed. Install the required dependencies using:

bash
Copy code
pip install -r requirements.txt
Run the Application

To run the application locally, execute:

bash
Copy code
streamlit run streamlit_app.py
This will start the Streamlit app, and you can access it in your web browser at http://localhost:8501.

Usage
Select a Stock Symbol:

Choose from popular stock symbols like META, NVDA, BABA, PYPL, and NFLX from the sidebar.
Alternatively, use the search bar to input a custom stock symbol.
View Live Data:

The app will display a table of the most recent intraday stock data, including opening price, high, low, close, and trading volume.
Check Option Prediction:

The app will predict whether a "Call" or "Put" option is more likely based on the recent price movements.
A probability bar will indicate the likelihood of each option.
Visualize Stock Data:

The closing prices are plotted on an interactive chart to help you visualize the stock's performance over time.
