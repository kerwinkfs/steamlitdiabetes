import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 

@st.cache_data
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_eda_app():
    st.subheader("Tidepool Data")
    df = load_data("data/diabetes_data_upload.csv")
    df_clean = load_data("data/diabetes_data_upload_clean.csv")
    freq_df = load_data("data/freqdist_of_age_data.csv")
    boluscdf1 = load_data("data/preprocessed/Bolus Calculator.csv")
    physicalactivitydf = load_data("data/preprocessed/Physical Activity.csv")
    fooddf = load_data("data/preprocessed/Food.csv")
    smbgdf = load_data("data/preprocessed/SMBG.csv")
    bolusdf = load_data("data/preprocessed/Bolus.csv")
    deviceeventdf = load_data("data/preprocessed/Device Event.csv")
    cgmdf = load_data("data/preprocessed/CGM.csv")
    basaldf = load_data("data/preprocessed/Basal.csv")
    
    submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
    if submenu == "Descriptive":
        st.subheader("Bolus Calcultor Data")
        st.dataframe(boluscdf1)
        with st.expander("Data Types"):
            st.dataframe(boluscdf1.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(boluscdf1.describe())
            
        st.subheader("Physical Activity Data")
        st.dataframe(physicalactivitydf)
        with st.expander("Data Types"):
            st.dataframe(physicalactivitydf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(physicalactivitydf.describe())
            
        st.subheader("Food Data")
        st.dataframe(fooddf)
        with st.expander("Data Types"):
            st.dataframe(fooddf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(fooddf.describe())
            
        st.subheader("Bolus Data")
        st.dataframe(bolusdf)
        with st.expander("Data Types"):
            st.dataframe(bolusdf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(bolusdf.describe())
            
        st.subheader("Basal Data")
        st.dataframe(basaldf)
        with st.expander("Data Types"):
            st.dataframe(basaldf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(basaldf.describe())
            
        st.subheader("Device Event")
        st.dataframe(deviceeventdf)
        with st.expander("Data Types"):
            st.dataframe(deviceeventdf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(deviceeventdf.describe())
            
        st.subheader("SMBG Data")
        st.dataframe(smbgdf)
        with st.expander("Data Types"):
            st.dataframe(smbgdf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(smbgdf.describe())
            
        st.subheader("CGM Data")
        st.dataframe(cgmdf)
        with st.expander("Data Types"):
            st.dataframe(cgmdf.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(cgmdf.describe())
        
    elif submenu == "Plots":
        st.subheader("Plots")
        # Layout
        col1,col2 = st.columns([2,1])
        with col1:
            with st.expander("Dist Plot of Gender"):
                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df)
                p01 = px.pie(gen_df,names='Gender Type',values='Counts')
                st.plotly_chart(p01,use_container_width=True)
            with st.expander("Dist Plot of Class"):
               gen_df = df['class'].value_counts().to_frame()
               gen_df = gen_df.reset_index()
               gen_df.columns = ['Class','Counts']
			   # st.dataframe(gen_df)
               p01 = px.pie(gen_df,names='Class',values='Counts')
               st.plotly_chart(p01,use_container_width=True)
               
        with col2:
            with st.expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())
        
        with st.expander("Frequency Dist Plot of Age"):
            p = px.bar(freq_df,x='Age',y='count')
            st.plotly_chart(p)
            
        with st.expander("Outlier Detection Plot"):
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)
            p3 = px.box(df,x='Age',color='Gender')
            st.plotly_chart(p3)
            
        with st.expander("Correlation Plot"):
            corr_matrix = df_clean.corr()
            fig = plt.figure(figsize=(20,10))
            sns.heatmap(corr_matrix,annot=True)
            st.pyplot(fig)
            p4 = px.imshow(corr_matrix)
            st.plotly_chart(p4)
        
    
