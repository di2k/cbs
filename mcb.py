import streamlit as st


def main():
    
    st.header('Metode Capital Budgeting')

    st.subheader('Payback Period (PP)')
    step = st.expander('Informasi')
    with step:
        st.markdown('#### Periode waktu yang menunjukkan berapa lama dana yang diinvestasikan akan bisa kembali')
        st.markdown(f"\n")
        st.markdown('#### Rumus:')
        st.markdown(
            r'#### <p style="text-align: center;font-size:1.15em">$${PP}=\frac{Investasi Awal}{Arus Kas} \times {1_{Tahun}}$$</p>', unsafe_allow_html=True)
        st.markdown('#### Kriteria:')
        st.markdown(r'Makin pendek <b><i>Payback Period</i></b> makin <b>baik</b>.', unsafe_allow_html=True)
        st.markdown(r'Jika <b><i>Payback Period</i></b> suatu investasi kurang dari <b><i>Payback Period</i></b> yang disyaratkan, maka usulan investasi layak diterima semua.', unsafe_allow_html=True)
        st.markdown('#### Batasan:')
        st.markdown(r'Metode <b><i>Payback Period</i></b> mengabaikan aliran kas masuk setelah periode <i>cut off.</i>', unsafe_allow_html=True)
        st.markdown(r'Metode <b><i>Payback Period</i></b> tidak mempertimbangkan <b>nilai waktu</b> uang.', unsafe_allow_html=True)

    st.subheader('Discounted Payback Period (DPP)')
    step = st.expander('Informasi')
    with step:
        st.markdown(r'#### Payback Period (PP) yang mempertimbangkan <i>time value of money</i>', unsafe_allow_html=True)
        st.markdown(f"\n")
        st.markdown(r'<b>DPP</b> mengacu pada periode waktu yang diperlukan untuk memulihkan pengeluaran kas awal dan dihitung dengan mendiskontokan arus kas yang akan dihasilkan di masa depan dan kemudian menjumlahkan nilai sekarang dari arus kas masa depan di mana diskon dilakukan dengan biaya rata-rata tertimbang. modal atau tingkat pengembalian internal.', unsafe_allow_html=True)        
        st.markdown('#### Rumus:')
        st.markdown(
            r'#### <p style="text-align: center;font-size:1.15em">$${DPP}={YBDP} + \frac{CCF}{DCF}$$</p>', unsafe_allow_html=True)
        st.markdown(r'$YBDP$ - Year Before the Discounted Payback Period Occurs')
        st.markdown(r'$CCF$ - Cumulative Cash Flow in Year Before Recovery')
        st.markdown(r'$DCF$ - Discounted Cash Flow in Year After Recovery')
        st.markdown('#### Kriteria:')
        st.markdown(r'Makin pendek <b><i>Discounted Payback Period</i></b> makin <b>baik</b>.', unsafe_allow_html=True)
        st.markdown('#### Batasan:')
        st.markdown(r'Metode <b><i>Discounted Payback Period</i></b> mengesampingkan pendapatan yang akan didapat setelah periode <i>payback</i> yang ditetapkan oleh perusahaan.', unsafe_allow_html=True)

             
    # st.markdown(
    #     r'### <p style="font-weight:500; margin-top:{5}px;margin-bottom:{0}px">Contoh PP: </p>', unsafe_allow_html=True)

    st.subheader('Net Present Value (NPV)')
    step = st.expander('Informasi')
    with step:
        st.markdown(r'#### Metode penilaian investasi yg menggunakan <i>discounted cash flow</i>.', unsafe_allow_html=True)
        st.markdown(f"\n")
        st.markdown(r'<b>NPV</b> merupakan <i>net benefit</i> yang telah didiskon dengan menggunakan <i>social opportunity cost of capital</i> sebagai diskon faktor.', unsafe_allow_html=True)
        st.markdown('#### Rumus:')
        st.markdown(r'### <p style="text-align: center;">$$NPV=\sum_{i=1}^n NB_i(1+i)^{-n}$$</p>', unsafe_allow_html=True)
        st.markdown(r'$NB$ - Net Benefit (benefit - cost)')
        st.markdown(r'$i$ - Diskon faktor')
        st.markdown(r'$n$ - tahun (waktu)')
        st.markdown('#### Kriteria:')
        st.markdown(r'<b>NPV > 0</b> (nol) ??? usaha/proyek layak (<i>feasible</i>) untuk dilaksanakan.', unsafe_allow_html=True)
        st.markdown(r'<b>NPV < 0</b> (nol) ??? usaha/proyek tidak layak (<i>un feasible</i>) untuk dilaksanakan>', unsafe_allow_html=True)
        st.markdown(r'<b>NPV = 0</b> (nol) ??? usaha/proyek berada dalam keadaan <i>BEP<i/> dimana R = TC dalam bentuk <i>present value</i>.', unsafe_allow_html=True)

    st.subheader('Equivalent Annual Annuity (EAA)')
    step = st.expander('Informasi')
    with step:
        st.markdown(r'#### EAA menghitung arus kas tahunan konstan yang dihasilkan oleh sebuah proyek selama umurnya.', unsafe_allow_html=True)
        st.markdown(f"\n")
        st.markdown('#### Rumus:')
        st.markdown(r'### <p style="text-align: center;">$$EAA=\frac{i  \times NPV}{{1 - (1 + i)}^{-n}}$$</p>', unsafe_allow_html=True)
        st.markdown(r'$i$ - Diskon faktor')
        st.markdown(r'$n$ - tahun (waktu)')
        st.markdown('#### Kriteria:')
        st.markdown(r'Pemilihan proyek dilakukan berdasarkan nilai EAA yang lebih besar.', unsafe_allow_html=True)

    st.subheader('Internal Rate of Return (IRR)')
    step = st.expander('Informasi')
    with step:
        st.markdown(r'#### IRR adalah <i>rate discount</i> dimana NPV dari proyek = 0.', unsafe_allow_html=True)
        st.markdown(f"\n")
        st.markdown(r'<b>IRR</b> merupakan <i>rate discount</i> dimana nilai <i>present value<i> dari <i>cash inflow</i> sama dengan nilai investasi awal suatu proyek.', unsafe_allow_html=True)
        st.markdown('#### Rumus:')
        st.markdown(r'### <p style="text-align: center;">$$IRR=i_1+\frac{NPV_1}{{(NPV_1}-{NPV_2)}}{(i_2 - i_1)}$$</p>', unsafe_allow_html=True)
        st.markdown(r'$i_1$ - Tingkat discount rate yang menghasilkan $NPV_1$')
        st.markdown(r'$i_2$ - Tingkat discount rate yang menghasilkan $NPV_2$')
        st.markdown('#### Kriteria:')
        st.markdown(r'Investasi diterima jika <b>IRR</b> yang dihasilkan lebih besar dibandingkan <i>cost of capital</i> (<b>COC</b>).', unsafe_allow_html=True)
        st.markdown(r'<b>IRR > COC</b> ??? usaha/proyek layak (<i>feasible</i>) untuk dilaksanakan.', unsafe_allow_html=True)
        st.markdown(r'<b>IRR < COC</b> ??? usaha/proyek tidak layak (<i>un feasible</i>) untuk dilaksanakan.', unsafe_allow_html=True)
        st.markdown(r'<b>IRR = COC</b> ??? usaha/proyek berada dalam keadaan <i>BEP<i/>.', unsafe_allow_html=True)

    st.subheader('Profitability Index (PI)')
    step = st.expander('Informasi')
    with step:
        st.markdown(r'#### Rasio antara PV arus kas masuk dan PV arus kas keluar.', unsafe_allow_html=True)
        st.markdown(f"\n")
        st.markdown(r'<b>PI</b> disebut juga dengan <i>benefit cost ratio</i>.', unsafe_allow_html=True)
        st.markdown('#### Rumus:')
        st.markdown(r'### <p style="text-align: center;">$$PI=\frac{PV Cash Inflows}{PV Cash Outflows}$$ atau $$PI=\frac{\sum_{t=0}^n\frac{CIF_t}{(1+k)^t}}{\sum_{t=0}^n\frac{COF_t}{(1+k)^t}}$$</p>', unsafe_allow_html=True)
        st.markdown(r'$CIF_t$ - Cash inflows pada periode t')
        st.markdown(r'$COF_t$ - Cash outflows pada periode t')
        st.markdown(r'k - Biaya modal')
        st.markdown(r't - Periode (waktu)')
        st.markdown('#### Kriteria:')
        st.markdown(r'<b>PI > 1</b> (satu) ??? usaha/proyek layak (<i>feasible</i>) untuk dilaksanakan.', unsafe_allow_html=True)
        st.markdown(r'<b>PI < 1</b> (satu) ??? usaha/proyek tidak layak (<i>un feasible</i>) untuk dilaksanakan.', unsafe_allow_html=True)
        st.markdown(r'<b>PI = 1</b> (satu) ??? usaha/proyek berada dalam keadaan <i>BEP<i/>.', unsafe_allow_html=True)

    