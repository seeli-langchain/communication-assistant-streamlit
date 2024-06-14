from models import Base, Person, Persona, Conversation, Message
from sqlalchemy.orm import Session
from typing import List
from connect import engine
from datetime import datetime

session = Session(bind=engine)

# Person & Contact

# Read
def get_main_person() -> Person:
    main_person = session.query(Person).filter(Person.is_main == True).first()

    if main_person:
        return main_person
    
    return create_main_person(first_name='First Name', last_name='Last Name')

def get_person_by_id(id: int) -> Person:
    return session.query(Person).get(id)

def get_contacts() -> List[Person]:
    return session.query(Person).filter(Person.is_main == False).all()

# Create
def create_main_person(first_name: str, last_name: str) -> Person:
    person = Person(first_name=first_name, last_name=last_name, is_main=True)
    session.add(person)
    session.commit()
    return person

def create_contact(first_name: str, last_name: str) -> Person:
    person = Person(first_name=first_name, last_name=last_name, is_main=False)
    session.add(person)
    session.commit()
    return person

# Update
def save_main_person(first_name: str, last_name: str, text: str) -> Person:
    person = get_main_person()
    person.first_name = first_name
    person.last_name = last_name
    person.text = text
    session.commit()
    return person

def save_person(id: int, first_name: str, last_name: str, text: str) -> Person:
    person = get_person_by_id(id)
    person.first_name = first_name
    person.last_name = last_name
    person.text = text
    session.commit()
    return person  

# Delete
def delete_person(id: int):
    person = get_person_by_id(id)
    session.delete(person)
    session.commit()

# Persona

# Read
def get_personas_of_main_person() -> List[Persona]:
    main_person = get_main_person()
    return main_person.personas

def get_persona_by_id(id: int) -> Persona:
    return session.query(Persona).get(id)

# Create
def add_persona_for_main_person() -> Persona:
    main_person = get_main_person()
    persona = Persona(text="", title="New Persona", person=main_person)
    session.add(persona)
    session.commit()
    return persona

# Update
def save_persona(id: int, text: str, title: str) -> Persona:
    persona = get_persona_by_id(id)
    persona.text = text
    persona.title = title
    session.commit()
    return persona

# Delete
def delete_persona(id: int):
    persona = get_persona_by_id(id)
    session.delete(persona)
    session.commit()

# Conversation
# Read
def get_conversations_of_main_person() -> List[Conversation]:
    main_person = get_main_person()
    return main_person.conversations

def get_conversation_by_id(id: int) -> Conversation:
    return session.query(Conversation).get(id)

# Create    
def create_conversation() -> Conversation:
    main_person = get_main_person()
    partner = main_person
    conversation = Conversation(person=main_person, partner=partner)
    session.add(conversation)
    session.commit()
    return conversation

# Update
def save_conversation(id: int, persona_id: int, partner_id: int, text: str, started_at: datetime ) -> Conversation:
    conversation = get_conversation_by_id(id)
    partner = get_person_by_id(partner_id)
    main_person = get_main_person()
    persona = get_persona_by_id(persona_id)
    conversation.partner = partner
    conversation.person = main_person
    conversation.persona = persona
    conversation.text = text
    conversation.started_at = started_at
    session.commit()
    return conversation

# Delete
def delete_conversation(id: int):
    conversation = get_conversation_by_id(id)
    session.delete(conversation)
    session.commit()

# Message

# Read

def get_messages_of_conversation(id: int) -> List[Message]:
    conversation = get_conversation_by_id(id)
    return conversation.messages

# get all messages of a conversation where the author is the main person
def get_own_messages_of_conversation(id: int) -> List[Message]:
    conversation = get_conversation_by_id(id)
    main_person = get_main_person()
    return [message for message in conversation.messages if message.author == main_person]

# get all messages of a conversation where the author is the partner
def get_received_messages_of_conversation(id: int) -> List[Message]:
    conversation = get_conversation_by_id(id)
    main_person = get_main_person()
    return [message for message in conversation.messages if message.author != main_person]

# get latest message of conversation
def get_latest_message_of_conversation(id: int) -> Message:
    conversation = get_conversation_by_id(id)
    return conversation.messages[-1]

# get latest own message of conversation
def get_latest_own_message_of_conversation(id: int) -> Message:
    own_messages = get_own_messages_of_conversation(id)
    return own_messages[-1]

# get latest received message of conversation
def get_latest_received_message_of_conversation(id: int) -> Message:
    received_messages = get_received_messages_of_conversation(id)
    return received_messages[-1]

def get_message_by_id(id: int) -> Message:
    return session.query(Message).get(id)

# Create
def create_received_message(conversation_id: int) -> Message:
    conversation = get_conversation_by_id(conversation_id)
    author_id = conversation.partner_id
    message = Message(conversation=conversation, author_id=author_id)
    session.add(message)
    session.commit()
    return message

def create_own_message(conversation_id: int) -> Message:
    conversation = get_conversation_by_id(conversation_id)
    author_id = conversation.person_id
    message = Message(conversation=conversation, author_id=author_id)
    session.add(message)
    session.commit()
    return message

# Update
def save_message(id: int, text: str, meta: str, draft: str, sent_at: datetime) -> Message:
    message = get_message_by_id(id)
    message.text = text
    message.meta = meta
    message.draft = draft
    message.sent_at = sent_at
    session.commit()
    return message

# Delete
def delete_message(id: int):
    message = get_message_by_id(id)
    session.delete(message)
    session.commit()





