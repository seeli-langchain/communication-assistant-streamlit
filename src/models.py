from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from datetime import datetime, date
from typing import Any, List

class Base(DeclarativeBase):
    pass

class Person(Base):
    __tablename__ = 'persons'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name:Mapped[str]
    last_name:Mapped[str]
    text:Mapped[str] = mapped_column(Text, nullable=True)	
    is_main:Mapped[bool] = mapped_column(default=False)
    personas: Mapped[List['Persona']] = relationship('Persona', back_populates='person')
    conversations: Mapped[List['Conversation']] = relationship('Conversation', back_populates='person', foreign_keys='Conversation.person_id')
    conversations_as_partner: Mapped[List['Conversation']] = relationship('Conversation', back_populates='partner', foreign_keys='Conversation.partner_id')

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Persona(Base):
    __tablename__ = 'personas'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_id:Mapped[int] = mapped_column(ForeignKey('persons.id'))
    title:Mapped[str] = mapped_column(Text, nullable=True)
    text:Mapped[str] = mapped_column(Text, nullable=True)	
    person:Mapped[Person] = relationship('Person', back_populates='personas')

    def __repr__(self) -> str:
        return f'{self.title}'

class Conversation(Base):
    __tablename__ = 'conversations'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    person_id:Mapped[int] = mapped_column(ForeignKey('persons.id'), nullable=False)
    persona_id:Mapped[int] = mapped_column(ForeignKey('personas.id'), nullable=True)
    partner_id:Mapped[int] = mapped_column(ForeignKey('persons.id'), nullable=False)
    text:Mapped[str] = mapped_column(Text, nullable=True)	
    started_at:Mapped[datetime] = mapped_column(default=datetime.now)

    person:Mapped[Person] = relationship('Person', foreign_keys=[person_id], 
                                         back_populates='conversations')
    persona:Mapped[Persona] = relationship('Persona', foreign_keys=[persona_id])
    partner:Mapped[Person] = relationship('Person', foreign_keys=[partner_id], 
                                          back_populates='conversations_as_partner')
    messages: Mapped[List['Message']] = relationship('Message', back_populates='conversation')

    def __repr__(self) -> str:
        return f'{self.id} conversation between {self.person.first_name} and {self.partner.first_name}'

class Message(Base):
    __tablename__ = 'messages'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    conversation_id:Mapped[int] = mapped_column(ForeignKey('conversations.id'), nullable=False)
    author_id:Mapped[int] = mapped_column(ForeignKey('persons.id'), nullable=False)
    title:Mapped[str] = mapped_column(Text, nullable=True)
    text:Mapped[str] = mapped_column(Text, nullable=True)
    meta:Mapped[str] = mapped_column(Text, nullable=True)
    draft:Mapped[str] = mapped_column(Text, nullable=True)
    sent_at:Mapped[datetime] = mapped_column(nullable=True)

    conversation: Mapped[Conversation] = relationship('Conversation', back_populates='messages')
    author: Mapped[Person] = relationship('Person')

    def __repr__(self) -> str:
        return f'{self.id} {self.text}'