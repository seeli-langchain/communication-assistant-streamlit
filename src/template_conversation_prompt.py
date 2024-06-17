from models import Base, Person, Persona, Conversation, Message
import persisting as repo
from datetime import datetime

def get_conversation_prompt(conversation: Conversation):

    title = conversation.title
    description = conversation.text
    date = conversation.started_at
    today = datetime.today()
    duration = today - date

    myself = conversation.person
    partner = conversation.partner
    conversation_start_info = ""

    last_partner_message = repo.get_latest_received_message_of_conversation(conversation.id)


    if (len(conversation.messages) > 1):

        started_by_me = myself == conversation.messages[0].author
        if (started_by_me):
            conversation_start_info = "The conversation was started by me "
        else:
            conversation_start_info = f"The conversation was started by my conversation partner {partner.first_name} "

        conversation_start_info += f"""on {date} and has been going on for {duration.days} days.
        
        """
        
        if (last_partner_message):
            conversation_start_info += f"The last message was sent by {partner.first_name} on {last_partner_message.sent_at}."
    else:
        conversation_start_info = "The conversation has not started yet and I am in the process of writing the first message."

    return f"""
    Here is the information about the conversation that I am having 
    with the {partner}
    
    Title: {title}
    Description: {description}

    {conversation_start_info}

    """