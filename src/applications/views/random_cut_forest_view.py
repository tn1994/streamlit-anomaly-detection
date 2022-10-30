import streamlit as st

from .base_view import spinner_wrapper
from ..services.random_cut_forest_service import RandomCutForestService


class RandomCutForestView:
    title = 'Random Cut Forest Service'

    @spinner_wrapper
    def main(self):
        st.title(self.title)

        random_cut_forest_service = RandomCutForestService()
        avg_codisp = random_cut_forest_service.main()
        if avg_codisp is not None:
            st.line_chart(random_cut_forest_service.data)
            st.line_chart(avg_codisp.values())
