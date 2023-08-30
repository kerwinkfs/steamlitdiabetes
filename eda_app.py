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
    st.subheader("EDA Section")
    df = load_data("data/diabetes_data_upload.csv")
    df_clean = load_data("data/diabetes_data_upload_clean.csv")
    freq_df = load_data("data/freqdist_of_age_data.csv")
    
    submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
    if submenu == "Descriptive":
        st.dataframe(df)
        with st.expander("Data Types"):
            st.dataframe(df.dtypes)
            
        with st.expander("Descriiptive Summary"):
            st.dataframe(df_clean.describe())
            
        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())
            
        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())
            
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
        
    