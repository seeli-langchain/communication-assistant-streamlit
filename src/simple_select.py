from models import Base, Person, Persona, Conversation, Message
from sqlalchemy.orm import Session
from connect import engine
from sqlalchemy import select

session = Session(bind=engine)

# get only the personens with the first name Markus
persons = session.query(Person).filter(Person.first_name == 'Markus').all()
# persons = session.query(Person).all()

#statement = select(Person).where(Person.first_name == 'Markus')
#result = session.execute(statement)

for person in persons:
    print(person)