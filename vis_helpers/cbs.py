import streamlit as st
from vis_helpers import hitung


def main():
    
    st.title('Capital Budgeting Simulator')

    st.markdown(r'Analisis investasi proyek dengan metode PP, NVP, IRR, PI', unsafe_allow_html=True)

    ci1, ci2, ci3 = st.columns(3)
    input_first_cash_flow = ci1.text_input("Cash Flow Proyek A", "-10000,9000,3000,1200")
    input_second_cash_flow = ci2.text_input("Cash Flow Proyek B", "-10000,1500,2000,2500,5000,5000")
    discount_rate = ci3.number_input("Discount Rate dalam %", 8)/100

    if(st.button('Submit')):

        input_first_cash_flow_list=input_first_cash_flow.split(",")
        first_cash_flow = [int(input_first_cash_flow_list[i]) for i in range(len(input_first_cash_flow_list))]

        if input_second_cash_flow == '':
            input_second_cash_flow = '0,0'
        input_second_cash_flow_list=input_second_cash_flow.split(",")
        second_cash_flow = [int(input_second_cash_flow_list[i]) for i in range(len(input_second_cash_flow_list))]

        st.subheader("Proyek A")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        if hitung.payback_period(first_cash_flow) == -1:
            col1.metric("PP", "NaN")
        else:
            col1.metric("PP", format(hitung.payback_period(first_cash_flow), '.2f'))
        if hitung.discounted_payback_period(first_cash_flow, discount_rate) == -1:
            col2.metric("DPP", "NaN")
        else:
            col2.metric("DPP", format(hitung.discounted_payback_period(first_cash_flow, discount_rate), '.2f'))
        col3.metric("NPV", format(hitung.net_present_value(first_cash_flow, discount_rate), '.2f'))
        if hitung.equivalent_annual_annuity(first_cash_flow, discount_rate) == -1:
            col4.metric("EAA", "NaN")
        else:
            col4.metric("EAA", format(hitung.equivalent_annual_annuity(first_cash_flow, discount_rate), '.2f'))
        col5.metric("IRR", format(hitung.internal_rate_of_return(first_cash_flow) * 100, '.2f')+ '%')
        col6.metric("PI", format(hitung.profitability_index(first_cash_flow, discount_rate), '.2f'))

        step = st.expander('Rincian Proyek A')
        with step:
            st.write('Cash Flows Proyek B: ',second_cash_flow)
            st.write('Discount Rate: ','\t\t\t',discount_rate * 100, ' %')

            if hitung.payback_period(first_cash_flow) == -1:
                st.write('Payback Period (PP): ','\t\t\t','nan')
            else:
                st.write('Payback Period (PP): ','\t\t\t',format(hitung.payback_period(first_cash_flow), '.2f'))
            if hitung.discounted_payback_period(first_cash_flow, discount_rate) == -1:
                st.write('Discounted Payback Period (DPP): ','\t','nan')
            else:
                st.write('Discounted Payback Period (DPP): ','\t',format(hitung.discounted_payback_period(first_cash_flow, discount_rate), '.2f'))
            st.write('Net Present Value (NPV): ','\t\t',format(hitung.net_present_value(first_cash_flow, discount_rate), '.2f'))
            if hitung.equivalent_annual_annuity(first_cash_flow, discount_rate) == -1:
                st.write('Equivalent Annual Annuity (EAA): ','\t','nan')
            else:
                st.write('Equivalent Annual Annuity (EAA): ','\t',format(hitung.equivalent_annual_annuity(first_cash_flow, discount_rate), '.2f'))
            st.write('Internal Rate of Return (IRR): ','\t',format(hitung.internal_rate_of_return(first_cash_flow) * 100, '.2f') + '%')
            st.write('Profitability Index (PI): ','\t\t',format(hitung.profitability_index(first_cash_flow, discount_rate), '.2f'))
            first_irr, second_irr, diff_cash_flow_irr, df_npv = hitung.npv_profile(first_cash_flow, second_cash_flow)


        if input_second_cash_flow != '0,0':

            st.subheader("Proyek B")
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            if hitung.payback_period(second_cash_flow) == -1:
                col1.metric("PP", "NaN")
            else:
                col1.metric("PP", format(hitung.payback_period(second_cash_flow), '.2f'))
            if hitung.discounted_payback_period(second_cash_flow, discount_rate) == -1:
                col2.metric("DPP", "NaN")
            else:
                col2.metric("DPP", format(hitung.discounted_payback_period(second_cash_flow, discount_rate), '.2f'))
            col3.metric("NPV", format(hitung.net_present_value(second_cash_flow, discount_rate), '.2f'))
            if hitung.equivalent_annual_annuity(second_cash_flow, discount_rate) == -1:
                col4.metric("EAA", "NaN")
            else:
                col4.metric("EAA", format(hitung.equivalent_annual_annuity(second_cash_flow, discount_rate), '.2f'))
            col5.metric("IRR", format(hitung.internal_rate_of_return(second_cash_flow) * 100, '.2f')+ '%')
            col6.metric("PI", format(hitung.profitability_index(second_cash_flow, discount_rate), '.2f'))

            step = st.expander('Rincian Proyek B')
            with step:
                st.write('Cash Flows Proyek B: ',second_cash_flow)
                st.write('Discount Rate: ','\t\t\t',discount_rate * 100, ' %')

                if hitung.payback_period(second_cash_flow) == -1:
                    st.write('Payback Period (PP): ','\t\t\t','nan')
                else:
                    st.write('Payback Period (PP): ','\t\t\t',format(hitung.payback_period(second_cash_flow), '.2f'))
                if hitung.discounted_payback_period(second_cash_flow, discount_rate) == -1:
                    st.write('Discounted Payback Period (DPP): ','\t','nan')
                else:
                    st.write('Discounted Payback Period (DPP): ','\t',format(hitung.discounted_payback_period(second_cash_flow, discount_rate), '.2f'))
                st.write('Net Present Value (NPV): ','\t\t',format(hitung.net_present_value(second_cash_flow, discount_rate), '.2f'))
                if hitung.equivalent_annual_annuity(second_cash_flow, discount_rate) == -1:
                    st.write('Equivalent Annual Annuity (EAA): ','\t','nan')
                else:
                    st.write('Equivalent Annual Annuity (EAA): ','\t',format(hitung.equivalent_annual_annuity(second_cash_flow, discount_rate), '.2f'))
                st.write('Internal Rate of Return (IRR): ','\t',format(hitung.internal_rate_of_return(second_cash_flow) * 100, '.2f') + '%')
                st.write('Profitability Index (PI): ','\t\t',format(hitung.profitability_index(second_cash_flow, discount_rate), '.2f'))
        csf = format(diff_cash_flow_irr * 100, '.2f') 
        st.subheader('Crossover Rate: '+csf+ '%')

        # hitung.plot_npv_profile(first_cash_flow, second_cash_flow)
        first_irr, second_irr, diff_cash_flow_irr, df_npv = hitung.npv_profile(first_cash_flow, second_cash_flow)





