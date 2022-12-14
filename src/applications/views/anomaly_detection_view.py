import uuid

import streamlit as st
import matplotlib.pyplot as plt

from .base_view import BaseView
from ..services.change_finder_service import generate_example_data
from ..services.change_finder_service import ChangeFinderService
from ..services.random_cut_forest_service import RandomCutForestService


class AnomalyDetectionView(BaseView):
    title: str = 'Anomaly Detection'

    key_sidebar_form: str = uuid.uuid1().__str__()

    def main(self):
        st.title(self.title)

        st.write('### Example Target Wave Data')
        example_data = self.get_data()
        if example_data is not None:
            st.line_chart(data=example_data)

        with st.sidebar.form(key=self.key_sidebar_form):
            r: float = st.slider('R', 0.01, 1.00, 0.01)
            order: int = st.slider('Order', 1, 10, 1)
            smooth: int = st.slider('Smooth', 3, 100, 3)
            submitted: bool = st.form_submit_button(
                label='Start Anomaly Detection')

        if None not in (r, order, smooth) and submitted:
            with st.spinner('Now Analysing...'):
                # Change Finder
                result: list = ChangeFinderService().analysis(
                    data=example_data, r=r, order=order, smooth=smooth)
                # Random Cut Forest
                random_cut_forest_service = RandomCutForestService()
                random_cut_forest_service.set_data(data=example_data)
                result_rcf: dict = random_cut_forest_service.main()

                if result is not None and result_rcf is not None:
                    st.write('### Result Score of Change Finder')
                    st.line_chart(result)
                    # self.plot_using_pyplot(result=result,
                    # example_data=example_data)  # other view

                    with st.expander(label='Raw Score Data'):
                        st.table(result)

                    st.write('### Result Score of Random Cut Forest')
                    st.line_chart(result_rcf.values())

                    with st.expander(label='Raw Score Data'):
                        st.table(result_rcf.values())

    @st.cache
    def get_data(self):
        return generate_example_data()

    @staticmethod
    def plot_using_pyplot(result, example_data):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(result)
        ax2 = ax.twinx()
        ax2.plot(example_data, 'r')
        plt.show()
        st.pyplot(fig=fig)
