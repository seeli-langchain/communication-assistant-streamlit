import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog
from datetime import date as date

class CrudDialog:

    dlg_title = "Received Message"

    # repo functions
    add_func = repo.create_received_message
    read_all_func = repo.get_conversations_of_main_person
    transfer_to_one = repo.get_latest_received_message_of_conversation
    read_one_func = repo.get_message_by_id
    delete_func = repo.delete_message
    save_func = repo.save_message

    def __init__(self, item):
        self.item = item
        self.id = item.id
        self.conversation_id = item.conversation_id
        self.title = item.title
        self.author = item.author
        self.author_id = item.author.id
        self.text = item.text
        self.sent_at = item.sent_at
        if self.sent_at is None:
            self.sent_at = date.today()

    def show_form(self):
    
        with st.form(key="form"):
            self.title = st.text_input("Title", value=self.title)
            self.text = st.text_area("Text", value=self.text, height=300)
            self.started_at = st.date_input("Received at", value=self.sent_at)
            
            buttons =  dlgs.add_buttons()
    
        dlgs.handle_buttons(buttons, self)
    
    def save(self):
        return CrudDialog.save_func(self.id, title=self.title, text=self.text, sent_at=self.sent_at)

crud_dialog.show(CrudDialog)

