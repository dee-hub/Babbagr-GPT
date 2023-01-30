from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import meta
from utils.st import (remote_css, local_css,)
import openai

print(st.session_state)
st.set_page_config(
        page_title="DraftAssist: The AI based writing partner",
        page_icon="logo.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )
col1, col2= st.columns([4, 6])
local_css("style.css")
with col1:
    from PIL import Image
    image = Image.open('logo.png')
    st.image(image, width=300)
    st.markdown(meta.SIDEBAR_INFO, unsafe_allow_html=True)
    with st.expander("Meet DraftAssist 👾", expanded=False):
        st.markdown(meta.STORY, unsafe_allow_html=True)

with col2:
    import streamlit as st
    st.title('DraftAssist 📝')
    st.write("Welcome to DraftAssist 🥳 v2.0")
    model_type = "text-davinci-003"      
    with st.expander("How to Use 👇", expanded=False):
        st.write("Example 1: DraftAssist can be used to generate creative and persuasive written content. For example, if we needed to write a persuasive letter to convince a potential customer to buy our product, we could use DraftAssist to generate text that is tailored to our requirements. \
                        \n\n Example 2: DraftAssist can also be used to generate cover letters for job applications. By providing DraftAssist with the job description, it can quickly generate a compelling cover letter that speaks directly to the employer's needs and requirements. \
                        \n\n Example 3: DraftAssist can also be used to generate newsletter content that is both interesting and informative. By providing DraftAssist with the desired topics and keywords, it can generate interesting content that speaks to what the reader wants to hear.")
    def check_password():
        """Returns `True` if the user had the correct password."""

        def password_entered():
            #Checks whether a password entered by the user is correct
            if st.session_state["password"] == st.secrets["access_code"]:
                st.session_state["password_correct"] = True
                del st.session_state["password"]  # don't store password
            else:
                st.session_state["password_correct"] = False

        if "password_correct" not in st.session_state:
            # First run, show input for password.
            st.text_input(
                "Access Code", type="password", on_change=password_entered, key="password"
            )
            return False

        elif not st.session_state["password_correct"]:
            # Password not correct, show input + error.
            st.text_input(
                "Password", type="password", on_change=password_entered, key="password"
            )
            st.error("😕 Access Code Incorrect: Contact the developer")
            return False
        else:
            # Password correct.
            return True

    if check_password():
        #access = st.text_input("Enter your access code", type="password")
        #access_code_secret = "oluwadolapo2023"
        #access_button = st.button('Access 🔐')
        #if access_button == True:
        #   if access == access_code_secret:
        text = st.text_area('Start writing here: ', height=100)
        generate = st.button('Idea 💡')
        if generate == True:
            openai.api_key = st.secrets["api_secret"]
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
            #st.warning('Incorrect Access Code. Contact the Developer ', icon="⚠️")
