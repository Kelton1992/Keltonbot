
import streamlit as st
import requests
import pandas as pd
import time

# --- Dashboard title ---
st.set_page_config(page_title="KeltonBot Dashboard")
st.title("💹 KeltonBot - Luno Trading Dashboard")

# --- Sidebar controls ---
st.sidebar.header("Controls")
start = st.sidebar.button("▶️ Start Bot")
stop = st.sidebar.button("⏹️ Stop Bot")

# --- Placeholder for chart and status ---
chart_placeholder = st.empty()
status_placeholder = st.empty()

# --- Data setup ---
data = pd.DataFrame(columns=["Time", "Price"])
api_url = "https://api.luno.com/api/1/ticker?pair=XBTZAR"

# --- Logic for bot ---
if start:
    st.sidebar.success("Bot started! Fetching live BTC/ZAR prices...")
    while True:
        try:
            response = requests.get(api_url).json()
            price = float(response["last_trade"])
            timestamp = time.strftime("%H:%M:%S")

            new_row = pd.DataFrame({"Time": [timestamp], "Price": [price]})
            data = pd.concat([data, new_row]).tail(30)

            chart_placeholder.line_chart(data.set_index("Time"))
            status_placeholder.info(f"💰 BTC/ZAR: R{price:,.2f}")

            time.sleep(5)
        except Exception as e:
            status_placeholder.error(f"Error: {e}")
            break

elif stop:
    st.sidebar.warning("Bot stopped.")
else:
    st.sidebar.info("Press ▶️ Start to begin fetching data.")
