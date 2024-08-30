import streamlit as st 
import pandas as pd 
import numpy as np  

def create_bar_chart():
    # Generating sample data  
    data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])  

    # Step 2: Creating a Bar Chart 
    st.subheader('Graphique à Barres')  
    st.write("Les graphiques à barres sont utiles pour comparer des données catégorielles.")  

    # Creates a bar chart from the provided data 
    st.bar_chart(data)  