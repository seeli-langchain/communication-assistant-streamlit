import streamlit as st
from models import Person, Persona, Conversation


def get_partner_prompt(conversation: Conversation):

    partner = conversation.partner
    info = partner.text

    prompt = f"""   
    Here is the information about the person that I am having the conversation with:
    Firstname: {partner.first_name}
    Lastname: {partner.last_name}

    Info: {info}
    """
    return prompt



 
