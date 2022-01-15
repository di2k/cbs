import streamlit as st
from vis_helpers import sidebar, authors, main_page, mcb, cbs

def main():
    """
    Main is responsible for the visualisation of everything connected with streamlit.
    It is the web application itself.
    """

    sidebar.sidebar_head()

    analysis_type = st.sidebar.selectbox("Navigasi", ['Beranda', 'Metode Capital Budgeting', 'Capital Budgeting Simulator'])

    if analysis_type == 'Beranda':
        main_page.main_page()
    elif analysis_type == 'Metode Capital Budgeting':
        mcb.main()
    elif analysis_type == 'Capital Budgeting Simulator':
        cbs.main()
    authors.show_developers()


if __name__ == '__main__':
    main()

    print("Streamlit finished it's work")