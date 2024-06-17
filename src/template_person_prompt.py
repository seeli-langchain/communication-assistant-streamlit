import streamlit as st
from models import Person, Persona, Conversation


def get_person_prompt(conversation: Conversation):

    person = conversation.person
    name = f"{person.first_name} {person.last_name}"
    info = person.text
    persona = conversation.persona

    prompt = f"""   
    Here is the information about myself that is relevant to the conversation:
    Name: {name}
    Info: {info}
    """

    if persona is not None:
        prompt += f"""
        
        In this conversation, I want you to consider the following additional 
        information about myself that is relevant in der context of this conversation:
        
        {persona.title}
        {persona.text}

        """
    return prompt



 
