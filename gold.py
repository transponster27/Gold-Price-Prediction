import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pickle
import yfinance as yf
import cufflinks as cf
import datetime

result = pickle.load(open(r"C:\Users\vrehm\OneDrive\Desktop\btech project\predict.pkl",'rb'))
gold_data = pickle.load(open(r"C:\Users\vrehm\OneDrive\Desktop\btech project\gold_price.pkl",'rb'))

st.title('Gold Price Predictor')

# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2011, 11, 18))
end_date = st.sidebar.date_input("End date", datetime.date(2019, 1, 1))

ticker_list = pd.DataFrame({'Gold ETF','S&P 500 Index',{'Dow Jones Index': "^DJI"},'Eldorado Gold Corporation (EGO)','EURO - USD Exchange Rate', 
                'Brent Crude Oil Futures','Crude Oil WTI USD', 'Silver Futures','US Bond Rate (10 years)','Platinum Price',
                'Palladium Price','Rhodium Prices','US Dollar Index','Gold Miners ETF','Oil ETF USO'})

tickerSymbol = st.sidebar.selectbox('Index ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(
    period='1d',
    start = '2011-11-18',
    end = '2019-01-01')

st.line_chart(tickerDf.Open)