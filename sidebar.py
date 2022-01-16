import streamlit as st
import vis_utils


def sidebar_head():
    """
    Sets Page title, page icon, layout, initial_sidebar_state
    Sets position of radiobuttons (in a row or one beneath another)
    Shows logo in the sidebar
    """
    st.set_page_config(
        page_title="Kelompok 1 | Capital Budgeting",
        page_icon="",
        layout="wide",
        initial_sidebar_state="auto"
    )


    html_code = vis_utils.show_sersitivis_logo(100, [1, 1, 1, 1], margin=[0, 0, 0, 0])
    st.sidebar.markdown(html_code, unsafe_allow_html=True)
    st.sidebar.markdown('')
    st.sidebar.markdown('')