import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import persisting as repo
from template import get_template
from models import Conversation


def get_response(conversation: Conversation):

    template = get_template(conversation)

    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI()
        
    chain = prompt | llm | StrOutputParser()
    
    return chain.invoke()

