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
                options=['Home','About','Predict','Contact','Source Code'],
                icons=['house-fill','person-circle','cpu','telephone-fill','code-slash'],
                menu_icon='flower3',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        if app == "Home":
            home.app()        
        if app == "About":
            about.app()
        if app == "Predict":
            predict.app()    
        if app == "Contact":
            contact.app()           
        if app == "Source Code":
            sourcecode.app()           
             
          
             
    run()            
         