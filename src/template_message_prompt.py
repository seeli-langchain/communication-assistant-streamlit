
from models import Base, Person, Persona, Conversation, Message


def get_message_prompt(conversation: Conversation):

    draft_message = conversation.messages[-1]

    if (draft_message.meta == None):
        meta_prompt = ""
    else:
        meta_prompt = f"""
    
    In order to create a message, I want you to be aware of the following meta information:
    This gives you an idea of the context in which the message is created. It explains my 
    intention behind creating and sending this message. This information should be confidential 
    and is just for you. Do not include this information as is in the content of the message.
    
    Knowing this will help you find the best possible wording for this message.

    {draft_message.meta}

    
    """
        
    prompt = f"""
    {meta_prompt}
    
    Here is the draft title and the draft content of the message that I came up with and that
    I want you to improve upon. 
    
    I want the resulting message constructive, fair and result oriented. 
    The receiver of this message should feel understood, motivated and should foster a continuing
    positive relationship between me an my communication partner.

    Draft title: {draft_message.title}
    Draft content: 
    {draft_message.draft}
    
    """

    return prompt
