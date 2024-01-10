from dotenv import load_dotenv
import os 
import streamlit as st
import google.generativeai as genai
import textwrap
import pathlib


from IPython.display import display , Markdown


def to_markdown(text):
    text = text.replace('.','*')
    return Markdown(textwrap.indent(text,prefix="> ",predicate=lambda_:True))


os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

def get_model_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

## St application


st.set_page_congig(page_title = 'Q & A Application')

st.header('Text to Text GEmini Appplication') 

input = st.text_input('Question:' , key='input')


submit = st.button('Ask anything')


if submit:
    response=get_model_response(input)
    st.subheader('The answer is')
    st.write(response)

