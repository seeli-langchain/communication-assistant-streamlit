from models import Base, Person, Persona, Conversation, Message
from template_system_prompt import get_system_prompt
from template_person_prompt import get_person_prompt
from template_partner_prompt import get_partner_prompt
from template_conversation_prompt import get_conversation_prompt
from template_history_prompt import get_conversation_history_prompt
from template_message_prompt import get_message_prompt

def get_template(conversation: Conversation):

    system_prompt = get_system_prompt()

    person_prompt = get_person_prompt(conversation)

    partner_prompt = get_partner_prompt(conversation)

    conversation_prompt = get_conversation_prompt(conversation)

    conversation_history = get_conversation_history_prompt(conversation)

    message_draft_prompt = get_message_prompt(conversation)

    return f"""
    
    system prompt: 
    {system_prompt}

    {person_prompt}

    {partner_prompt}

    conversation:
    {conversation_prompt}

    conversation history: 
    {conversation_history}

    information about the message to be create:
    {message_draft_prompt}

    """