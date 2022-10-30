import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

from ..services.isolation_forest_service import IsolationForestService


class IsolationForestView:
    """
    ref: https://github.com/streamlit/streamlit/issues/4573
    """
    title = 'Isolation Forest Service'

    def main(self):
        st.title(self.title)

        isolation_forest_service = IsolationForestService()

        df = isolation_forest_service.main()
        if df is not None:
            # original
            plt.figure(figsize=(8, 8))
            ax = sns.scatterplot(
                x="feat1",
                y="feat2",
                data=df,
                palette='bright')
            st.pyplot(ax.get_figure())

        if st.button(label='Isolation Cut Forest'):
            # result
            plt.figure(figsize=(8, 8))
            ax = sns.scatterplot(
                x="feat1",
                y="feat2",
                data=df,
                hue='predict',
                palette='bright')
            st.pyplot(ax.get_figure())
