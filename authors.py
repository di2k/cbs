import streamlit as st
import vis_utils

authors_css = """
        style='
        display: block;
        margin-bottom: 0px;
        margin-top: 60px;
        padding-top: 60px;
        font-size:1.1em;
        filter: brightness(85%);
        text-align: center;
        text-decoration: none;
        '
"""

def made_by():
    """
    Shows formatted 'by'
    """
    st.sidebar.header(f"\n\n\n\n\n\n")

    st.sidebar.markdown(
        '<p ' + authors_css + '>' + 'Oleh: <br><b>Kelompok I</b> </p>',
        unsafe_allow_html=True)
    st.sidebar.markdown(f"\n\n")
    html_code = vis_utils.show_logo(55, [1, 1, 1, 1], margin=[0, 0, 0, 22])
    st.sidebar.markdown(html_code, unsafe_allow_html=True)

def show_developers():
    """
    Shows all the links and mails to developers
    :return:
    """
    made_by()
