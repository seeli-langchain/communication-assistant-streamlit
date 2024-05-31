from models import Base, Person, Persona, Conversation, Message
from connect import engine

print('Creating tables')
Base.metadata.create_all(bind=engine)