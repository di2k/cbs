import numpy as np
import pandas as pd
import numpy_financial as npf
import matplotlib.pyplot as plt


def payback_period(period_cashflow):
    '''
    Payback Period
    ==============
    Menghitung Jangka waktu yang dibutuhkan untuk mengembalikan modal.
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM 
    return:
        payback_period
    '''
    if len(period_cashflow) == 0:
        return -1
    df = pd.DataFrame(enumerate(period_cashflow), columns=['Period', 'Cash Flow'])
    df['Cumulative Cash Flows'] = df['Cash Flow'].cumsum()
    df['pct'] = np.abs(df['Cumulative Cash Flows'].shift()/df['Cash Flow'])
    df['Last Period'] = df['Period'].shift()
    df['Payback Period'] = df['Last Period'] + df['pct']
    df_positive = df[df['Cumulative Cash Flows']>=0]
    if df_positive.shape[0] == 0:
        return -1
    min_period = df_positive['Period'].min()
    payback_period = df[df['Period'] == min_period]['Payback Period'].iloc[0]
    return payback_period
    
def discounted_payback_period(period_cashflow, discount_rate):
    '''
    Dicounted Payback Period
    ========================
    Menghitung Jangka waktu yang dibutuhkan untuk mengembalikan modal pada nilai saat ini (NPV).
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM [0.1 for 10%]
    return:
        discounted_payback_period:
    '''
    if len(period_cashflow) == 0:
        return -1
    df = pd.DataFrame(enumerate(period_cashflow), columns=['Period', 'Cash Flow'])
    df['Present Value'] = df.apply(lambda row:row['Cash Flow'] / np.power((1+discount_rate), row['Period']),axis=1)
    df['Cumulative Discounted Cash Flows'] = df['Present Value'].cumsum()
    df['pct'] = np.abs(df['Cumulative Discounted Cash Flows'].shift()/df['Present Value'])
    df['Last Period'] = df['Period'].shift()
    df['Discounted Payback Period'] = df['Last Period'] + df['pct']
    df_positive = df[df['Cumulative Discounted Cash Flows']>=0]
    if df_positive.shape[0] == 0:
        return -1
    min_period = df_positive['Period'].min()
    discounted_payback_period = df[df['Period'] == min_period]['Discounted Payback Period'].iloc[0]
    return discounted_payback_period

def net_present_value(period_cashflow, discount_rate):
    '''
    Net Present Value (NPV)
    =======================
    Menghitung nilai seluruh cash flow pada saat ini
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM [0.1 for 10%]
    return:
        df['Present Value'].sum()
    '''
    if len(period_cashflow) == 0:
        return -1
    df = pd.DataFrame(enumerate(period_cashflow), columns=['Period', 'Cash Flow'])
    df['Present Value'] = df.apply(lambda row:row['Cash Flow'] / np.power((1+discount_rate), row['Period']),axis=1)
    return df['Present Value'].sum()

def df_npv(period_cashflow, discount_rate):
    '''
    Dataframe Net Present Value (NPV)
    =================================
    Menampilkan dataframe nilai seluruh cash flow pada saat ini
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM [0.1 for 10%]
    return:
        df
    '''
    if len(period_cashflow) == 0:
        return -1
    df = pd.DataFrame(enumerate(period_cashflow), columns=['Period', 'Cash Flow'])
    df['Present Value'] = df.apply(lambda row:row['Cash Flow'] / np.power((1+discount_rate), row['Period']),axis=1)
    return df

def equivalent_annual_annuity(period_cashflow, discount_rate):
    '''
    Equivalent Annual Annuity (EAA)
    ===============================
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM 
    return:
        NPV/PVIFA: EAA
    '''
    n = len(period_cashflow) - 1
    # if n =0, EAA = NPV/0. 
    if n < 0 or n == 0:
        return -1
    NPV = net_present_value(period_cashflow, discount_rate)
    PVIFA = (1 - (1/np.power((1+discount_rate),n)))/discount_rate
    return NPV/PVIFA

def internal_rate_of_return(period_cashflow):
    '''
    Internal Rate of Return (IRR)
    =============================
    Parameter:
        period_cashflow: [CF_0, ... , CF_n] 
        discount_rate: Discount Rate (r) can based on CAPM 
    return:
        npf.irr(period_cashflow): IRR
    '''
    if len(period_cashflow) == 0:
        return -1
    return npf.irr(period_cashflow)

def profitability_index(period_cashflow, discount_rate):
    '''
    Profitability Index (PI)
    ========================
    Parameter:
        period_cashflow: [CF_0, ... , CF_n]
        discount_rate: Discount Rate (r) can based on CAPM 
    return:
        PI: Profitability Index
    '''
    if len(period_cashflow) == 0:
        return -1
    NPV = net_present_value(period_cashflow, discount_rate)
    if NPV == 0:
        return -1
    cost = period_cashflow[0]*(-1)
    PI = (NPV+cost)/cost
    return PI

def npv_profile(PA_cash_flow, PB_cash_flow):
    '''
    NPV Profile
    ===========
    Kurva hubungan antara NPV dan biaya modal
    Sensitivity Analytics the NPV value by move Discount Rate from 0% to 100%
    Parameter:
        PA_cash_flow: The first project's cash flow. [CF_0, ... , CF_n] 
        PB_cash_flow: The second project's cash flow. [CF_0, ... , CF_n]  
    Function call: 
        internal_rate_of_return: IRR calculation function calculate based on Cash flow
    return:
        first_irr: The first project's IRR
        second_irr: The first project's IRR 
        diff_cash_flow_irr: The difference of the two cash flows' IRR
            df_cash_flow: (First project cash flows - relative second project cash flow)
        df_npv: Create a data frame for NPV profile plot. ["Discount Rate","Project A", "Project B"]
    '''
    npv_list = []
    for discount_rate in np.arange(0, 1.01, 0.01):
        first_npv = net_present_value(PA_cash_flow, discount_rate)
        second_npv = net_present_value(PB_cash_flow, discount_rate)
        npv_list.append([discount_rate, first_npv, second_npv])
    df_npv = pd.DataFrame(npv_list, columns=["Discount Rate","Project A", "Project B"])
    # NPV = 0, for IRR
    first_irr = internal_rate_of_return(PA_cash_flow)
    second_irr = internal_rate_of_return(PB_cash_flow)
    # before calulate the differ
    df_cash_flow = pd.DataFrame({
        "Project A":pd.Series(PA_cash_flow), 
        "Project B":pd.Series(PB_cash_flow)
        }).fillna(0)
    df_cash_flow['Diff Cash Flow'] = df_cash_flow["Project A"] - df_cash_flow["Project B"]
    diff_cash_flow = list(df_cash_flow['Diff Cash Flow'])
    # Cross over rate
    diff_cash_flow_irr = internal_rate_of_return(diff_cash_flow)
    return first_irr, second_irr, diff_cash_flow_irr, df_npv

def plot_npv_profile(PA_cash_flow, PB_cash_flow):
    if PB_cash_flow == [0,0]:
        first_irr, second_irr, diff_cash_flow_irr, df_npv = npv_profile(PA_cash_flow, PB_cash_flow)
        plt.figure(figsize=(9,6))

        plt.axhline(y=0, c='gray', linestyle='dashed')
        plt.axvline(x=diff_cash_flow_irr, c='gray', linestyle='dashed')

        plt.plot(df_npv['Discount Rate'], df_npv['Project A'], label='Project A')
        
        plt.title("NPV Profile (Sensitivity Test for NPV)", fontsize=14)
        plt.xlabel('Discount Rate (r)')
        plt.ylabel('NPV (in dollar)')
        plt.legend()
        plt.show()
    else:
        first_irr, second_irr, diff_cash_flow_irr, df_npv = npv_profile(PA_cash_flow, PB_cash_flow)
        plt.figure(figsize=(9,6))

        plt.axhline(y=0, c='gray', linestyle='dashed')
        plt.axvline(x=diff_cash_flow_irr, c='gray', linestyle='dashed')

        plt.plot(df_npv['Discount Rate'], df_npv['Project A'], label='Project A')
        plt.plot(df_npv['Discount Rate'], df_npv['Project B'], label='Project B')
        
        plt.title("NPV Profile (Sensitivity Test for NPV)", fontsize=14)
        plt.xlabel('Discount Rate (r)')
        plt.ylabel('NPV (in dollar)')
        plt.legend()
        plt.show()
