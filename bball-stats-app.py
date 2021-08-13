import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np

st.title('NBA Player Stats:')

st.markdown("""
Performs simple webscrapping of NBA player stats and displays data!
* **Python libraries:** base64, pandas, streamlmit
* **Data source:** [Basketball-reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2022))))


# Web scrapping NBA player stats

# Sidebar - Team selection 
# Sidebar - Position selection
# Data filtering
# DL NBA player stats 
# Heatmap    
