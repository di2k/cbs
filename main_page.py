import streamlit as st
import vis_utils


def main_page():
    sersitivis_logo = vis_utils.show_sersitivis_logo(width=65, padding=[0, 0, 20, 25], margin=[0, 0, 30, 0])
    st.markdown(sersitivis_logo, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center;'><b>Capital Budgeting Simulator</b></h1>", unsafe_allow_html=True)  
    st.markdown("<h3 style='text-align: center;'>Program analisis investasi proyek metode PP, DPP, NPV, EAA, IRR, PI</h3>", unsafe_allow_html=True)  
    st.markdown(f"\n\n\n")
    # st.markdown("<h4 style='text-align: center;'>Kelompok I</h4>", unsafe_allow_html=True)  

    step = st.expander('Oleh:',expanded=True)

    with step:
        st.markdown("<h5>Kelompok I</h5>", unsafe_allow_html=True)  
        col1, col2 = st.columns(2)
        col1.markdown('91121083 - Arif Hidayat')
        col1.markdown('91121092 - Arif Rachman')
        col1.markdown('91121094 - Didik Setiawan')
        col1.markdown('91121096 - Fawazi Bahtiar Ahmad')

        col2.markdown('91121097 - Ganjar Adi Pradana')
        col2.markdown('91121099 - Krisna Permadi')
        col2.markdown('91121100 - Muhammad Fauzan H')
        col2.markdown('91121102 - Rezha Murthy')

    
    # cols = st.beta_columns((1, 6, 2))
    # with cols[1]:
    #     st.header("An Application for fast and easy data processing and visualisation")
    
    # cols = st.beta_columns((3, 3, 1))
    # with cols[1]:
    #     st.header("By")
    #     st.markdown("")
    #     st.markdown("")
    #     st.markdown("")
    #     st.markdown("")
    
    # sersitive_logo = vis_utils.show_logo(width=55, padding=[0, 0, 0, 0], margin=[0, 0, 0, 0])
    # st.markdown(sersitive_logo, unsafe_allow_html=True)
    
    # st.markdown("")
    # st.markdown("")
    # st.markdown("")
