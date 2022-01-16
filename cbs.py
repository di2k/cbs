import streamlit as st
import hitung
import pandas as pd




def main():
    
    st.title('Capital Budgeting Simulator')

    st.markdown(r'<b>Analisis investasi proyek dengan metode PP, DPP, NPV, EAA, IRR, PI</b>', unsafe_allow_html=True)
    st.markdown(r'Isi <i>Cash Flow</i> dengan pembatas tiap tahun menggunakan tanda koma ( , )', unsafe_allow_html=True)
    st.markdown(r'Klik <b>Submit</b> untuk melakukan proses simulasi.', unsafe_allow_html=True)

    ci1, ci2, ci3 = st.columns(3)
    input_first_cash_flow = ci1.text_input("Cash Flow Proyek A", "-10000,9000,3000,1200")
    input_second_cash_flow = ci2.text_input("Cash Flow Proyek B", "-10000,1500,2000,2500,5000,5000")
    discount_rate = ci3.number_input("Discount Rate dalam %", step=1e-2, format="%.2f", value=8.00)/100

    if(st.button('Submit')):

        input_first_cash_flow_list=input_first_cash_flow.split(",")
        first_cash_flow = [int(input_first_cash_flow_list[i]) for i in range(len(input_first_cash_flow_list))]

        if input_second_cash_flow == '':
            input_second_cash_flow = '0,0'
        input_second_cash_flow_list=input_second_cash_flow.split(",")
        second_cash_flow = [int(input_second_cash_flow_list[i]) for i in range(len(input_second_cash_flow_list))]

        first_irr, second_irr, diff_cash_flow_irr, df_npv = hitung.npv_profile(first_cash_flow, second_cash_flow)
        csf = format(diff_cash_flow_irr * 100, '.2f') 
        dr = format(discount_rate * 100, '.2f') 
        st.markdown(r"<b>Discount Rate: "+dr+ "</b>%", unsafe_allow_html=True)

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



        # df1 = hitung.df_npv(first_cash_flow, discount_rate)
        # st.dataframe(df1)
        # df2 = hitung.df_npv(second_cash_flow, discount_rate)
        # st.dataframe(df2)
        # frames = [df1, df2]
        # df =  pd.concat(frames, keys=['A', 'B'])
        # st.dataframe(df)


        step = st.expander('Rincian Proyek A')
        with step:
            st.markdown(r'Cash Flows <b>Proyek A</b>: ', unsafe_allow_html=True)
            st.write('Discount Rate: ','\t\t\t',discount_rate * 100, ' %')
            
            df1 = hitung.df_npv(first_cash_flow, discount_rate)
            st.dataframe(df1)
            # st.line_chart(df1['Present Value'])

            if hitung.payback_period(first_cash_flow) == -1:
                st.write('Payback Period (PP): ','\t\t\t','nan')
            else:
                st.write('Payback Period (PP): ','\t\t\t',format(hitung.payback_period(first_cash_flow), '.2f')+' tahun')
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

        if input_second_cash_flow != '0,0':

            st.subheader("Proyek B")
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            if hitung.payback_period(second_cash_flow) == -1:
                col1.metric("PP", "NaN")
            else:
                col1.metric("PP", format(hitung.payback_period(second_cash_flow), '.2f'), format(hitung.payback_period(second_cash_flow) - hitung.payback_period(first_cash_flow), '.2f'), delta_color="inverse")
            if hitung.discounted_payback_period(second_cash_flow, discount_rate) == -1:
                col2.metric("DPP", "NaN")
            else:
                col2.metric("DPP", format(hitung.discounted_payback_period(second_cash_flow, discount_rate), '.2f'), format(hitung.discounted_payback_period(second_cash_flow, discount_rate) - hitung.discounted_payback_period(first_cash_flow, discount_rate), '.2f'), delta_color="inverse")
            col3.metric("NPV", format(hitung.net_present_value(second_cash_flow, discount_rate), '.2f'), format(hitung.net_present_value(second_cash_flow, discount_rate) - hitung.net_present_value(first_cash_flow, discount_rate), '.2f'))
            if hitung.equivalent_annual_annuity(second_cash_flow, discount_rate) == -1:
                col4.metric("EAA", "NaN")
            else:
                col4.metric("EAA", format(hitung.equivalent_annual_annuity(second_cash_flow, discount_rate), '.2f'), format(hitung.equivalent_annual_annuity(second_cash_flow, discount_rate) - hitung.equivalent_annual_annuity(first_cash_flow, discount_rate), '.2f'))
            col5.metric("IRR", format(hitung.internal_rate_of_return(second_cash_flow) * 100, '.2f')+ '%', format((hitung.internal_rate_of_return(second_cash_flow) - hitung.internal_rate_of_return(first_cash_flow)) * 100, '.2f') + '%')
            col6.metric("PI", format(hitung.profitability_index(second_cash_flow, discount_rate), '.2f'), format(hitung.profitability_index(second_cash_flow, discount_rate) - hitung.profitability_index(first_cash_flow, discount_rate), '.2f'))

            step = st.expander('Rincian Proyek B')
            with step:
                st.markdown(r'Cash Flows <b>Proyek B</b>: ', unsafe_allow_html=True)
                st.write('Discount Rate: ','\t\t\t',discount_rate * 100, ' %')
                
                df2 = hitung.df_npv(second_cash_flow, discount_rate)
                st.dataframe(df2)
                # st.line_chart(df2['Present Value'])

                if hitung.payback_period(second_cash_flow) == -1:
                    st.write('Payback Period (PP): ','\t\t\t','nan')
                else:
                    st.write('Payback Period (PP): ','\t\t\t',format(hitung.payback_period(second_cash_flow), '.2f') + ' tahun')
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

        st.markdown(r"<b>Crossover Rate: "+csf+ "</b>%", unsafe_allow_html=True)

        # hitung.plot_npv_profile(first_cash_flow, second_cash_flow)
        first_irr, second_irr, diff_cash_flow_irr, df_npv = hitung.npv_profile(first_cash_flow, second_cash_flow)
        
        st.markdown("<h5 style='text-align: center;'>NPV Profile</h5>", unsafe_allow_html=True)  
        st.markdown("<p style='text-align: center;'> (Sensitivity Test for NPV)</p>", unsafe_allow_html=True)  

        st.line_chart(df_npv)

        # chart = (
        # alt.Chart(
        #     data=df_npv,
        #     title="Your title",
        # )
        # .mark_line()
        # .encode(
        #     x=alt.X("Discount Rate", axis=alt.Axis(title="Discount Rate")),
        #     y=alt.Y("Project A", axis=alt.Axis(title="Project A")),
        # ))

        # st.altair_chart(chart)






