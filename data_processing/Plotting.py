import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


class Plotters:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.plot_func = None

    def any_to_any(self, col1: str, col2: str | None = None, **kwargs):
        """
        Handles both 1-column histograms and 2-column plots.
        Extra settings like bins or color can be passed through kwargs.
        """
        if self.plot_func is None:
            raise NotImplementedError("Subclasses must define self.plot_func")

        fig, ax = plt.subplots()

        if col2 is None:
            self.plot_func(data=self.data, x=col1, ax=ax, **kwargs)
            ax.set_title(f"Distribution of {col1}")
        else:
            self.plot_func(data=self.data, x=col1, y=col2, ax=ax, **kwargs)
            ax.set_title(f"{col1} vs {col2}")

        st.pyplot(fig)
        plt.close(fig)


class BarCharts(Plotters):
    def __init__(self, data: pd.DataFrame):
        super().__init__(data=data)
        self.plot_func = sns.barplot


class HistCharts(Plotters):
    def __init__(self, data: pd.DataFrame):
        super().__init__(data=data)
        self.plot_func = sns.histplot
