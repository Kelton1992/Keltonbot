import streamlit as st
import pandas as pd
import time
import random

st.set_page_config(page_title="Luno Trading Dashboard", layout="wide")

st.title("💹 Kelton Luno Trading Dashboard")

# Sidebar controls
st.sidebar.header("Controls")
start = st.sidebar.button("▶️ Start Bot")
stop = st.sidebar.button("⏹️ Stop Bot")

# Placeholder for chart data
chart_placeholder = st.empty()

# Create initial DataFrame
data = pd.DataFrame({"Price": [random.uniform(1000, 1200)]})

if start:
    st.sidebar.success("Bot started...")
    for i in range(50):
        new_row = {"Price": data["Price"].iloc[-1] + random.uniform(-10, 10)}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        chart_placeholder.line_chart(data)
        time.sleep(0.2)

elif stop:
    st.sidebar.warning("Bot stopped.")
else:
    chart_placeholder.line_chart(data)
