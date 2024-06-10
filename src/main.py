import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from persisting import get_main_person


load_dotenv()

# app config
st.set_page_config(page_title="Communication Assistant", page_icon="🤖")
st.title("Communication Assistant")


st.sidebar.success("select a page above")