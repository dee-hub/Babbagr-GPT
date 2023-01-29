from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import meta
from utils.st import (remote_css, local_css,)
import openai
import pyperclip 

print(st.session_state)
st.set_page_config(
        page_title="DraftAssist: The AI based writing partner",
        page_icon="👾",
        layout="wide",
        initial_sidebar_state="expanded"
    )
col1, col2= st.columns([4, 6])
local_css("style.css")
with col1:
    from PIL import Image
    image = Image.open('robot2.jpg')
    st.image(image, width=300)
    st.markdown(meta.SIDEBAR_INFO, unsafe_allow_html=True)
    with st.expander("Meet DraftAssist 👾", expanded=False):
        st.markdown(meta.STORY, unsafe_allow_html=True)

with col2:
    st.markdown(meta.HEADER_INFO, unsafe_allow_html=True)
    access = st.text_input("Enter your access code", type="password")
    access_code_secret = st.secrets["access_code"]
    access_button = st.button('Access 🔐')
    if access_button:
        if access == access_code_secret:
            st.write("Welcome to DraftAssist 🥳")
            model_type = "text-davinci-003"      
            with st.expander("How to Use 👇", expanded=False):
                st.write("Example 1: DraftAssist can be used to generate creative and persuasive written content. For example, if we needed to write a persuasive letter to convince a potential customer to buy our product, we could use DraftAssist to generate text that is tailored to our requirements. \
\n\n Example 2: DraftAssist can also be used to generate cover letters for job applications. By providing DraftAssist with the job description, it can quickly generate a compelling cover letter that speaks directly to the employer's needs and requirements. \
\n\n Example 3: DraftAssist can also be used to generate newsletter content that is both interesting and informative. By providing DraftAssist with the desired topics and keywords, it can generate interesting content that speaks to what the reader wants to hear.")
            text = st.text_area('Start writing here: ', height=100)
            generate = st.button('Idea 💡')
            if generate:
                openai.api_key = st.secrets["api_key"]
                generated_text_initial = openai.Completion.create(model=model_type, prompt=text, temperature=0.9, max_tokens=2000)
                generated_text = generated_text_initial["choices"][0]['text']
            #generated_text = generated_text.replace('\n', '')
            #generated_text = generated_text.replace(', '')
            #texts = text + generated_text
            #text = st.text_area("Start writing here", texts)
                result = st.write("Results \n", generated_text)
            #copy = st.button('Copy to Clipboard 📝')
            #if copy:
             #   pyperclip.copy(generated_text)
              #  st.success('Copied!')
                with st.expander("API Results", expanded=False):
                    st.write(generated_text_initial)
            else:
                st.write('Some error occurred')
        else:
            st.warning('Incorrect Access Code. Contact the Developer ', icon="⚠️")
