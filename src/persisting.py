from models import Base, Person, Persona, Conversation, Message
from sqlalchemy.orm import Session
from typing import List
from connect import engine

session = Session(bind=engine)

def get_main_person() -> Person:
    main_person = session.query(Person).filter(Person.is_main == True).first()

    if main_person:
        return main_person
    
    return create_main_person(first_name='First Name', last_name='Last Name')
    
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

def get_person_by_id(person_id: int) -> Person:
    return session.query(Person).get(person_id)

def get_contacts() -> List[Person]:
    return session.query(Person).filter(Person.is_main == False).all()

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

def get_personas_of_main_person() -> List[Persona]:
    main_person = get_main_person()
    return main_person.personas

def get_conversations_of_main_person() -> List[Conversation]:
    main_person = get_main_person()
    return main_person.conversations

def add_persona_for_main_person(text: str) -> Persona:
    main_person = get_main_person()
    persona = Persona(text="", title="New Persona", person=main_person)
    session.add(persona)
    session.commit()
    return persona

def get_persona_by_id(persona_id: int) -> Persona:
    return session.query(Persona).get(persona_id)

def save_persona(persona_id: int, text: str, title: str) -> Persona:
    persona = get_persona_by_id(persona_id)
    persona.text = text
    persona.title = title
    session.commit()
    return persona

def delete_persona(persona_id: int):
    persona = get_persona_by_id(persona_id)
    session.delete(persona)
    session.commit()

def delete_person(person_id: int):
    person = get_person_by_id(person_id)
    session.delete(person)
    session.commit()
