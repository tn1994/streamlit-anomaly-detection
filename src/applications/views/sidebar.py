import logging

import streamlit as st

from .base_view import spinner_wrapper
from .anomaly_detection_view import AnomalyDetectionView
from .isolation_forest_view import IsolationForestView
from .random_cut_forest_view import RandomCutForestView

from ..services.version_service import VersionService

logger = logging.getLogger(__name__)


class Sidebar:

    def __init__(self):
        self.service_dict = {
            'anomaly_detection_service': self.anomaly_detection_service,
            'isolation_forest_view': self.isolation_forest_service,
            'random_cut_forest_service': self.random_cut_forest_service,
            'version_service': self.version_service,
        }

    def main(self):
        radio_value = st.sidebar.radio('Sub Page', self.service_dict.keys())
        if radio_value:
            select_service = self.service_dict[radio_value]
            select_service()

    @staticmethod
    def anomaly_detection_service():
        anomaly_detection_view = AnomalyDetectionView()
        anomaly_detection_view.main()

    @staticmethod
    def isolation_forest_service():
        isolation_forest_view = IsolationForestView()
        isolation_forest_view.main()

    @staticmethod
    def random_cut_forest_service():
        random_cut_forest_view = RandomCutForestView()
        random_cut_forest_view.main()

    @spinner_wrapper
    def version_service(self):
        st.title('Version Service')
        version_service = VersionService()

        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label='Python Version',
                      value=version_service.get_python_version())
        with c2:
            st.metric(
                label='Pip Version',
                value=version_service.get_pip_version())
        with c3:
            st.metric(
                label='Streamlit Version',
                value=version_service.get_library_version(
                    library_name='streamlit'))
        st.download_button(label='Download requirements.txt',
                           data=version_service.get_pip_list(format='freeze'),
                           file_name='requirements.txt',
                           mime='text/txt')
        pip_list = version_service.get_pip_list(format='json')
        with st.expander('Pip List', expanded=True):
            st.table(pip_list)
