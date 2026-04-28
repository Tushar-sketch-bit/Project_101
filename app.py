import streamlit as st
import pandas as pd
import numpy as np
from IO_operations.i_o import DataLoader
from data_processing.Plotting import BarCharts, HistCharts

st.set_page_config(page_title="Analysis dashboard", layout="wide")
st.title("Analysis Dashboard")
st.markdown("---")

@st.cache_data
def load_data(location):
    return DataLoader.load_data(file_path=location)

def plot_Bar_chart(df, col1, col2):
    chart = BarCharts(data=df)          #
    return chart.any_to_any(col1=col1, col2=col2)

def plot_Histogram_chart(df, col1, bins):
    chart = HistCharts(data=df)       
    return chart.any_to_any(col1=col1, col2=None, bins=bins)


uploaded = st.file_uploader("upload CSV ", type=["csv"])

if uploaded is None:
    st.info("upload CSV file to proceed")
    st.stop()

df = pd.read_csv(uploaded)
st.success(f"Loaded: {len(df)} rows x {len(df.columns)} columns")

num_cols = df.select_dtypes(include=np.number).columns.tolist()
all_cols = df.columns.tolist()

tab1, tab2, tab3 = st.tabs(["Data", "Bar Chart", "Histogram"])

with tab1:
    st.dataframe(df.head(20), use_container_width=True)

with tab2:
    col1 = st.selectbox("X axis", all_cols, key="b1")
    col2 = st.selectbox("Y axis", num_cols, key="b2")
    if st.button("Plot"):
        plot_Bar_chart(df, col1, col2)

with tab3:
    col1 = st.selectbox("Column", num_cols, key="h1")
    bins = st.slider("Bins", 5, 100, 20)
    if st.button("Plot", key="hbtn"):
        plot_Histogram_chart(df, col1, bins)