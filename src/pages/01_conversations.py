import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog

class CrudDialog:

    dlg_title = "Conversation"

    # repo functions
    add_func = repo.create_conversation
    read_all_func = repo.get_conversations_of_main_person
    transfer_to_one = repo.get_conversation_by_id
    read_one_func = repo.get_conversation_by_id
    delete_func = repo.delete_conversation
    save_func = repo.save_conversation

    def __init__(self, item):
        self.item = item
        self.id = item.id
        self.person = item.person
        self.partner_id = item.partner.id
        if (item.persona is not None):
            self.persona_id = item.persona.id
        else: 
            self.persona_id = None
        self.text = item.text
        self.started_at = item.started_at

    def show_form(self):

        personas = repo.get_personas_of_main_person()
        contacts = repo.get_contacts()

        if (self.persona_id is None):
            idx1 = None
        else:
            idx1 = [item.id for item in personas].index(self.persona_id)
        
        if (self.person.id == self.partner_id):
            idx2 = None
        else:
            idx2 = [item.id for item in contacts].index(self.partner_id)
    
        with st.form(key="form"):
            
            self.persona_id = st.selectbox("persona", [item.id for item in personas], 
                           format_func=lambda x: repo.get_persona_by_id(x), index=idx1, 
                           placeholder="Select an persona for this conversation", label_visibility="collapsed")
     
            self.partner_id = st.selectbox("partner", [item.id for item in contacts], 
                           format_func=lambda x: repo.get_person_by_id(x), index=idx2, 
                           placeholder="Select the conversation partner", label_visibility="collapsed")
     

            self.started_at = st.date_input("Started at", value=self.started_at)
            self.text = st.text_area("Text", value=self.text, height=200)
            buttons =  dlgs.add_buttons()
    
        dlgs.handle_buttons(buttons, self)
    
    def save(self):
        return CrudDialog.save_func(self.id, self.persona_id, self.partner_id, self.text, self.started_at)

crud_dialog.show(CrudDialog)

