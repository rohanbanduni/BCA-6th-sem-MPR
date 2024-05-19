import streamlit as st

from streamlit_option_menu import option_menu
import os

import home, about, contact, predict, sourcecode
st.set_page_config(page_title="PlantCare", page_icon="🪴")




class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='PlantCare ',
                options=['Home','About Us','Predict','Contact','Source Code'],
                icons=['house-fill','person-circle','cpu','telephone-fill','code-slash'],
                menu_icon='flower3',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "lightblue"},
        "nav-link-selected": {"background-color": "lightgreen"},}
                
                )

        if app == "Home":
            home.app()        
        if app == "About Us":
            about.app()
        if app == "Predict":
            predict.app()    
        if app == "Contact":
            contact.app()           
        if app == "Source Code":
            sourcecode.app()           
             
          
             
    run()            
         