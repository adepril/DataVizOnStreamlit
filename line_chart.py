import streamlit as st 
import pandas as pd 
import numpy as np  

def create_line_chart():
    # Generating sample data  
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])  

    # Step 1: Creating a Line Chart  
    st.subheader('Graphique Linéaire') 
    st.write("Les graphiques linéaires sont excellents pour visualiser les tendances au fil du temps.") 

    # Creates a line chart from the provided data.
    st.line_chart(data)  