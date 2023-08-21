import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
model_loaded = pickle.load(open('saved_steps.pkl', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    # Heart Disease Prediction Page
if (selected == 'Pneumonia Prediction'):
    
    # page title
    st.title('Pnuemonia Prediction using ML')
    
    col1, col2, col3 = st.columns(1)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')