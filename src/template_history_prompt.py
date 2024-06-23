
from models import Base, Person, Persona, Conversation, Message


def get_conversation_history_prompt(conversation: Conversation):

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
        Message from: {message.author} sent at {message.sent_at}: 

        {message.title}
        
        {message.text}

        """

    return prompt

