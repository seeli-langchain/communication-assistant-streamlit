import streamlit as st
import pandas as pd
import numpy as np

def add_buttons(number_of_buttons = 5):

    number_of_additional_buttons = number_of_buttons - 5

    columns = st.columns(number_of_buttons)
    buttons = []
    for i in range(5):
        
        if (i == 0):
            buttons.append(columns[i].form_submit_button("➕"))
        elif (i == 1):
             buttons.append(columns[i].form_submit_button("🗑️"))
        elif (i == 2):
             buttons.append(columns[i].form_submit_button("💾"))
        elif (i == 3):
             buttons.append(columns[i].form_submit_button("✖️"))
        elif (i == 4):          
             buttons.append(columns[i].form_submit_button("✔️"))
        
    for i in range(number_of_additional_buttons):
         buttons.append(columns[5 + i].form_submit_button(f"But{5+i}"))
    print(buttons)
    return buttons



def handle_buttons(buttons):
    buttons
    for i in range(len(buttons)):
        if (buttons[i]):
            if (i == 0): 
                print("New")
            elif (i == 1):
                print("Delete")
            elif (i == 2):
                print("Save")
            elif (i == 3):
                print("Cancel")
            elif (i == 4):
                print("Save and Close")
            else:   
                print(f"Button {i} pressed")

            print(f"Button {i} pressed")



with st.form(key="form"):
        buttons = []
        title = st.text_input("Title" )
        text = st.text_area("Text",height=200)
        buttons =  add_buttons(6)
        print("----------------------------------")
        print(type(buttons))
        handle_buttons(buttons)

