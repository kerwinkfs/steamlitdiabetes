import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 

def process_medap_file(dataset1):
    
    dataset1['INVAMT'] = pd.to_numeric(dataset1['INVAMT'], errors='coerce')

    filterdata = dataset1[dataset1['INVAMT'] > 0]

    dupdata = filterdata[filterdata.duplicated(['invoice no', 'INVAMT'])]

    filterdupdata = dupdata[['Vendor Name', 'INVAMT']].copy()

    groupdata = filterdupdata.groupby(['Vendor Name'])['INVAMT'].sum().reset_index()

    sortdata = groupdata.sort_values('INVAMT', ascending = False)

    sortdata['INVAMT'] = sortdata['INVAMT'].apply(lambda x: "${:.1f}k".format((x/1000)))

    dupdata1 = filterdata[filterdata.duplicated(['Vendor Number', 'INVAMT'])]

    filterdupdata1 = dupdata1[['Vendor Name', 'INVAMT']].copy()

    groupdata1 = filterdupdata1.groupby(['Vendor Name'])['INVAMT'].sum().reset_index()

    sortdata1 = groupdata1.sort_values('INVAMT', ascending = False)

    sortdata1['INVAMT'] = sortdata1['INVAMT'].apply(lambda x: "${:.1f}k".format((x/1000)))

    dupdata2 = filterdata[filterdata.duplicated(['Vendor Number', 'INVAMT', 'invoice no'])]

    filterdupdata2 = dupdata2[['Vendor Name', 'INVAMT']].copy()

    groupdata2 = filterdupdata2.groupby(['Vendor Name'])['INVAMT'].sum().reset_index()

    sortdata2 = groupdata2.sort_values('INVAMT', ascending = False)

    dataset1 = dataset1.head(10)
    filterdata = filterdata.head(10)
    amountcost = groupdata1['INVAMT'].sum()
    amountcost = "${:,.0f}k".format((amountcost/1000))
    
    return dataset1, sortdata1, amountcost

@st.cache_data
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_medap_app():
    
    st.subheader("Med AP Insight")
    
    dataset1 = load_data("data/medapfile.csv")
    
    dataset, filterdata, amountcost = process_medap_file(dataset1)
    
    st.subheader("Accounts Payable Data")
    with st.expander("Raw Data"):
        st.dataframe(dataset)
    with st.expander("Data Columns"):
        st.dataframe(dataset.columns) 
    with st.expander("Descriiptive Summary"):
        st.dataframe(dataset.describe())
        
    st.subheader("Accounts Payable Dup Analysis Data")
    with st.expander("Potenial amount to be recovered"):
        st.text(amountcost)
    with st.expander("Top vendor prospect"):
        st.dataframe(filterdata)
            
    