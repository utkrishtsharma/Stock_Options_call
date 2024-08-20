import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
from prediction_bot import predict_option  # Import the prediction function

# Set up API key and URL for fetching stock data
API_KEY = "W31KYKUK3Q4J3C01"
BASE_URL = "https://www.alphavantage.co/query"

# Title of the app
st.title("Live Stock Data App")

# Brief description for users
st.write("""
## Overview
This application allows you to fetch and visualize live intraday stock data. Simply select a stock from the sidebar or search for a specific stock symbol to view the latest price movements and closing prices. Additionally, the app will predict whether a "Call" or "Put" option is more likely.
""")

# Sidebar for stock options
st.sidebar.header("Stock Options")

# Predefined stock options
stocks = {
    "Meta Platforms, Inc. (META)": "META",
    "NVIDIA Corporation (NVDA)": "NVDA",
    "Alibaba Group Holding Limited (BABA)": "BABA",
    "PayPal Holdings, Inc. (PYPL)": "PYPL",
    "Netflix, Inc. (NFLX)": "NFLX"
}

# Display stock options as buttons
stock_symbol = st.sidebar.radio("Choose a stock to view:", list(stocks.values()), index=0)

# Search bar for custom stock symbol input
st.sidebar.write("### Or search for a specific stock:")
custom_symbol = st.sidebar.text_input("Enter stock symbol")
search_button = st.sidebar.button("Search")

# Function to fetch live stock data from Alpha Vantage API
def fetch_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "5min",
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Check if the data retrieval was successful
    if "Time Series (5min)" not in data:
        st.error("Failed to retrieve data. Please check the stock symbol or try again later.")
        return None

    # Convert JSON data to DataFrame
    time_series = data['Time Series (5min)']
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df

# Determine which symbol to use: predefined or custom
symbol_to_use = stock_symbol
if search_button and custom_symbol:
    symbol_to_use = custom_symbol.upper()

# Fetch and display data if a stock symbol is selected
if symbol_to_use:
    df = fetch_stock_data(symbol_to_use)
    
    if df is not None:
        st.write(f"Displaying data for {symbol_to_use}")
        
        # Display the first few rows of the data table
        st.write("""
        ### Stock Data Table
        Below is the table displaying the most recent intraday stock data for the selected symbol:
        - **Time:** The timestamp for each 5-minute interval.
        - **Open:** The opening price of the stock at the start of the 5-minute interval.
        - **High:** The highest price of the stock during the 5-minute interval.
        - **Low:** The lowest price of the stock during the 5-minute interval.
        - **Close:** The closing price of the stock at the end of the 5-minute interval.
        - **Volume:** The number of shares traded during the 5-minute interval.
        """)
        st.dataframe(df.head())

        # Plotting the closing prices using Matplotlib
        st.write("""
        ### Closing Prices Chart
        The chart below shows the closing prices of the stock over time, helping you visualize the price movements throughout the day.
        """)
        fig, ax = plt.subplots()
        ax.plot(df.index, df['4. close'], label='Close Price')
        ax.set_title(f"{symbol_to_use} Closing Prices")
        ax.set_xlabel("Time")
        ax.set_ylabel("Price")
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

        # Predict "Call" or "Put" option
        probabilities = predict_option(df)
        put_prob, call_prob = probabilities

        # Display prediction results
        st.write("### Option Prediction")
        st.write(f"Call Option Probability: **{call_prob:.2f}**")
        st.write(f"Put Option Probability: **{put_prob:.2f}**")

        # Create a probability bar
        st.write("### Option Probability Indicator")
        st.progress(call_prob)  # This shows the probability as a progress bar
        st.write("Move left for Put, right for Call:")
        st.progress(put_prob)
