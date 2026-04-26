import streamlit as st
import requests
from IO_operations.i_o import DataLoader
from data_processing.Plotting import BarCharts
from data_processing.Plotting import HistCharts



st.set_page_config(page_title="Analysis dashboard",layout= "wide")

@st.cache_data
def load_data(location):
 return DataLoader.load_data(file_path = location)


def plot_Bar_chart(col1, col2):
  return BarCharts.any_to_any(col1=col1, col2=col2)


def plot_Histogram_chart(col1, col2, bins):
  return HistCharts.any_to_any(col1=col1, col2=col2, bins=bins)











