import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stocks from Yahoo Finance

Show Closing Price Selected!

""")

tickerSymbol = st.text_input("Select ticker: ", 'GOOGL') # in python variable=input() # example input:'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf =  tickerData.history(period='1d',start='2010-5-31',end= '2022-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
st.subheader('ivan@cienciaydatos.es')