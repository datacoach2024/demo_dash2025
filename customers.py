import pandas as pd
import plotly.express as px
import streamlit as st

from connect import set_connection

# with set_connection() as psg
# min_date, max_date = 

with st.sidebar:
    edate = st.date_input(
        label = 'Select report date',
        min_value = '2025-01-01',
        max_value = '2025-03-13',
        value = '2025-03-13'
    )

with open('queries/customers.sql') as f:
    custs_query = f.read().format(report_date = edate)

st.write(custs_query)