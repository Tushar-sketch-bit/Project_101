import streamlit as st
import pandas as pd
import numpy as np
import ollama
from IO_operations.i_o import DataLoader
from data_processing.Plotting import BarCharts, HistCharts

st.set_page_config(page_title="Analysis dashboard", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "df" not in st.session_state:
    st.session_state.df = None

@st.cache_data
def load_data(location):
    return DataLoader.load_data(file_path=location)

def plot_Bar_chart(df, col1, col2):
    chart = BarCharts(data=df)
    return chart.any_to_any(col1=col1, col2=col2)

def plot_Histogram_chart(df, col1, bins):
    chart = HistCharts(data=df)
    return chart.any_to_any(col1=col1, col2=None, bins=bins)

# Chat history 
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

#File upload 
if st.session_state.df is None:
    with st.chat_message("assistant"):
        st.write("Upload the CSV file and ask me anything about the data!!!")
        uploaded = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded:
            st.session_state.df = pd.read_csv(uploaded)
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"✅ File Uploaded: {len(st.session_state.df)} rows × {len(st.session_state.df.columns)} columns"
            })
            st.rerun()

#after file upload
if st.session_state.df is not None:
    df = st.session_state.df

    st.markdown("---")
    st.title("Analysis Dashboard")
    st.markdown("---")

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

    st.markdown("---")

    # ── Chat input
    user_input = st.chat_input("Ask me anything about the data...")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    context = f"Dataset: {len(df)} rows, columns: {list(df.columns)}\n{df.describe().to_string()}"
                    messages = [{"role": "system", "content": context}] + st.session_state.messages
                    response = ollama.chat(model="llama2", messages=messages)
                    reply = response["message"]["content"]
                    st.write(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                except Exception as e:
                    st.error(f"Ollama error: {e}")