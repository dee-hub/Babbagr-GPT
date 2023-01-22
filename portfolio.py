from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import meta
import config
from utils.st import (remote_css, local_css,)
import openai

print(st.session_state)
st.set_page_config(
        page_title="Dee the Writing Assistant",
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
    with st.expander("Here is how to make me help you 👇", expanded=False):
        st.markdown(meta.STORY, unsafe_allow_html=True)

with col2:
    st.markdown(meta.HEADER_INFO, unsafe_allow_html=True)
    st.markdown(meta.CHEF_INFO, unsafe_allow_html=True)
    chef = st.selectbox("Choose your prefered writing companion", index=1, options=["Curie", "Babbage", "Davinci"])
    if chef == "Babbage":
        model_type = "text-babbage-001"
        with st.expander("About me 👇", expanded=False):
            st.write("I am good at picking up obvious patterns in text and then using that as a reference to generate text. \
                I can also perform broad classification tasks like assigning categories to industries, genres and media content. \
                    For creative applications, I am able to understand enough structure to create simple plots and titles.")
        
        token_length = st.selectbox("Select a token length (how long you want the generated text to be)", index=3, options=[None, 10, 30, 60, 80, 100, 130, 150])
        temperature = st.selectbox("Select how diverse you want each idea to be. Try 0.9 for more creative applications, and 0 for ones with a well-defined answer.", index=2, options=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        with st.expander("How to Use 👇", expanded=True):
            st.write("I can be used for \n\n 1) Idea iteration e.g. you can type a prompt as simple as “Provide 7 tips to promote my blog” and I will automatically create a list of practical advice. \
                    You can do this for just about any topic that is reasonably well known. \
                        This can either provide standalone content or be used as a starting point \
                            for a more in-depth tutorial. \n\n 2) Sentence completion: I can work as a great brainstorming tool and help you complete your thoughts. \
                    If you start a paragraph or sentence, I can quickly get the context and serve as a \
                        writing assistant. \n\n 3) Plot generation: If you provide me with a list of plot ideas from a specific genre, \
                    I can continue adding to that list. If you select the good ones and delete the others, \
                        you can keep sending the growing list to me and improve the results.")
        text = st.text_area('Start writing here: ', height=100)

        generate = st.button('Idea 💡')
        if generate:
            openai.api_key = config.api_key
            generated_text_initial = openai.Completion.create(model=model_type, prompt=text, temperature=temperature, max_tokens=token_length)
            generated_text = generated_text_initial["choices"][0]['text']
            generated_text = generated_text.replace('\n\n', '\n')
            #generated_text = generated_text.replace(', '')
            #texts = text + generated_text
            #text = st.text_area("Start writing here", texts)
            text = st.text_area("Results", generated_text, height=300)

            with st.expander("API Results", expanded=False):
                st.write(generated_text_initial)