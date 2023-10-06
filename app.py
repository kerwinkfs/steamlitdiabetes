import streamlit as st 
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app
from medap_app import run_medap_app
from PIL import Image

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Kx Solutions Data App </h1>
		<h4 style="color:white;text-align:center;">Data Insights</h4>
		</div>
		"""
desc_temp = """
			### Kx Solutions Data App
App Content
- EDA Section: Exploratory Data Analysis of Data
- ML Section: ML Predictor App
- MEDAP Section: Accounts Payable Analysis
			"""
  
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def main():
	
    st.set_page_config(page_title="Kxsolutions Demo", page_icon=":robot:")
    
    #st.title("Main App")
    stc.html(html_temp)
    
    my_logo = add_logo(logo_path="data/kxlogo.png", width=70, height=60)
    st.sidebar.image(my_logo)
    
    menu = ["Home","EDA","ML","MEDAP","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        st.write(desc_temp)
    elif  choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    elif choice == "MEDAP":
        run_medap_app()
    else:
        st.subheader("About")
        st.text("Learn More - Todo")
    
if __name__ == '__main__':
    main()
