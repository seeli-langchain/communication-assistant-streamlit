import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog

class CrudDialog:

    dlg_title = "Contact"

    # repo functions
    add_func = repo.create_contact
    read_all_func = repo.get_contacts
    read_one_func = repo.get_person_by_id
    delete_func = repo.delete_person
    save_func = repo.save_person

    def __init__(self, item):
        self.item = item
        self.id = item.id
        self.first_name = item.first_name
        self.last_name = item.last_name
        self.text = item.text

    def show_form(self):
    
        with st.form(key="form"):
            col1, col2 = st.columns(2)
            self.first_name = col1.text_input("First Name", value=self.first_name)
            self.last_name = col2.text_input("Last Name", value=self.last_name)
            self.text = st.text_area("Text", value=self.text, height=200)
            buttons =  dlgs.add_buttons()
    
        dlgs.handle_buttons(buttons, self)
    
    def save(self):
        return CrudDialog.save_func(self.id, self.first_name, self.last_name, self.text)

crud_dialog.show(CrudDialog)

