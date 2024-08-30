import streamlit as st 
import pandas as pd 
import numpy as np  

def create_area_chart():
    # Generating sample data  
    data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])  

    # Step 3: Creating an Area Chart 
    st.subheader('Graphique en Aires')  
    st.write("Les graphiques en aires aident à montrer les tendances cumulatives des données.")

    # Creates an area chart from the provided data 
    st.area_chart(data)  