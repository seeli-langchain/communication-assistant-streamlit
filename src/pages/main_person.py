import streamlit as st
import persisting as repo

main_person = repo.get_main_person()

st.title("Main Person")

first_name = st.text_input("First Name", value=main_person.first_name)
last_name = st.text_input("Last Name", value=main_person.last_name)

text = st.text_area("Text", value=main_person.text, height=300)

if st.button("Save"):
    repo.save_main_person(first_name, last_name, text)
    st.success("Saved")


