import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog

class CrudDialog:

    dlg_title = "Persona"

    # repo functions
    add_func = repo.add_persona_for_main_person
    read_all_func = repo.get_personas_of_main_person
    transfer_to_one = repo.get_persona_by_id
    read_one_func = repo.get_persona_by_id
    delete_func = repo.delete_persona
    save_func = repo.save_persona

    def __init__(self, item):
        self.item = item
        self.id = item.id
        self.title = item.title
        self.text = item.text

        self.extra_left = ["Miau"]
        self.extra_right = ["Wuff", "Quack"]
        self.func_left = [self.do_miau]
        self.func_right = [self.do_wuff, self.do_quack]

    def do_miau(self):
        st.write("Miau")
    
    def do_wuff(self):
        st.write("Wuff")
    
    def do_quack(self):
        st.write("Quack")


    def show_form(self):
    
        with st.form(key="form"):
            self.title = st.text_input("Title", value=self.title)
            self.text = st.text_area("Text", value=self.text, height=200)
            buttons =  dlgs.add_buttons(extra_left=self.extra_left, extra_right=self.extra_right)
    
        dlgs.handle_buttons(buttons, self, self.func_left, self.func_right)
    
    def save(self):
        return CrudDialog.save_func(self.id, self.text, self.title)

crud_dialog.show(CrudDialog)
