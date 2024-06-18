import streamlit as st
import persisting as repo
import helper_dlgs as dlgs
import crud_dialog
from datetime import date as date
from llm_interaction import get_response

class CrudDialog:

    dlg_title = "Draft new Message"

    # repo functions
    add_func = repo.create_own_message
    read_all_func = repo.get_conversations_of_main_person
    transfer_to_one = repo.get_latest_own_message_of_conversation
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
        self.meta = item.meta
        self.draft = item.draft
        self.text = item.text
        self.sent_at = item.sent_at
        #if self.sent_at is None:
        #    self.sent_at = date.today()
        self.extra_left = ["Generate"]
        self.extra_right = []
        self.func_left = [self.generate_text]
        self.func_right = []

    def generate_text(self):
        self.save()
        if self.draft is None:
            st.warning("Please write a draft first.")
            st.stop()
        
        generated_text = get_response(self.item.conversation)
        self.text = generated_text
        self.save()
            
    def show_form(self):
        with st.form(key="form"):
            self.title = st.text_input("Title", value=self.title)
            self.meta = st.text_area("Meta-Information about the message", value=self.meta, height=150)
            self.draft = st.text_area("Draft text of message", value=self.draft, height=300)
            self.text = st.text_area("Text", value=self.text, height=300)
            self.started_at = st.date_input("Sent at", value=self.sent_at)
            
            buttons =  dlgs.add_buttons(extra_left=self.extra_left, extra_right=self.extra_right)
    
        dlgs.handle_buttons(buttons, self, self.func_left, self.func_right)
    
    def save(self):
        return CrudDialog.save_func(self.id, title=self.title, text=self.text, 
                                    meta=self.meta, draft=self.draft, sent_at=self.sent_at)

crud_dialog.show(CrudDialog)

