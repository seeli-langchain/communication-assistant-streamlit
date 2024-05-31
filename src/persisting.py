from models import Base, Person, Persona, Conversation, Message
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

person1 = Person(first_name='Markus', last_name='Seeli')
person2 = Person(first_name='Joshua', last_name='Bushnell')

session.add(person1)
session.add(person2)

session.commit()
