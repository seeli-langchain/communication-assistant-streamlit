import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog as dlg


#main_person = repo.get_main_person()

##dlgs.manage_state()

class Repo:
    add_func = repo.add_persona_for_main_person
    read_all_func = repo.get_personas_of_main_person
    read_one_func = repo.get_persona_by_id
    delete_func = repo.delete_persona
    save_func = repo.save_persona

    dlg_title = "Persona"

    def __init__(self, item):
        self.item = item
        self.id = item.id
        self.title = item.title
        self.text = item.text

    def show_form(self):
    
        with st.form(key="form"):
            self.title = st.text_input("Title", value=self.title)
            self.text = st.text_area("Text", value=self.text, height=200)
            buttons =  dlgs.add_buttons()
    
        dlgs.handle_buttons(buttons, self)
    
    def save(self):
        return Repo.save_func(self.id, self.text, self.title)

dlg.show(Repo)








