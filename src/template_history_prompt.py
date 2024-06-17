
from models import Base, Person, Persona, Conversation, Message


def get_conversation_history(conversation: Conversation):

    messages = conversation.messages[0:-1]

    if (len(messages) == 0):
        return """
        There are no messages in this conversation yet.
        
        """

    prompt = """

    Here is the history of the conversation:

    """

    for message in messages:
        prompt += f"""
        --------------------------------	
        Message from: {message.sender.name} sent at {message.sent_at}: 

        {message.title}
        
        {message.text}

        """

    return prompt

