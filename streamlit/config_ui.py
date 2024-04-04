import streamlit as st

import gradio as gr
import time
# from storyblocks.config.api_db import get_api_key, set_api_key
from storyblocks.config.api_db import get_api_key, set_api_key
from storyblocks.api_utils.eleven_api import getCharactersFromKey


def onShow(button_text):
    if button_text == "Show":
        return gr.Textbox.update(type="text"), gr.Button.update(value="Hide")
    return gr.Textbox.update(type="password"), gr.Button.update(value="Show")

def verify_eleven_key(eleven_key, remaining_chars):
    if (eleven_key and get_api_key('ELEVEN LABS') != eleven_key):
        try:
            return getCharactersFromKey(eleven_key)
        except Exception as e:
            raise gr.Error(e.args[0])
    return remaining_chars

def saveKeys(openai_key, eleven_key, a1111):
    if (get_api_key('OPENAI') != openai_key):
        set_api_key("OPENAI", openai_key)
    if (get_api_key('A1111') != a1111):
        set_api_key("A1111", a1111)
    if (get_api_key('ELEVEN LABS') != eleven_key):
        set_api_key("ELEVEN LABS", eleven_key)
        return  gr.Textbox.update(value=openai_key),\
                gr.Textbox.update(value=eleven_key),\
                gr.Textbox.update(value=a1111),\
                

    return  gr.Textbox.update(value=openai_key),\
            gr.Textbox.update(value=eleven_key),\
            gr.Textbox.update(value=a1111),\
            gr.Radio.update(visible=True)

def getElevenRemaining(key):
    if(key):
        try:
            return getCharactersFromKey(key)
        except Exception as e:
            return e.args[0]
    return ""
def create_config_ui():
    with st.container():
        with st.columns(3):
            openai_key = st.text_input(
                "OPENAI API KEY",
                type="password",
                value=get_api_key("OPENAI"),
                show_copy_button=True
            )
            show_openai_key = st.button("Show")
            if show_openai_key:
                openai_key = st.text_input(
                    "OPENAI API KEY",
                    value=get_api_key("OPENAI"),
                    show_copy_button=True
                )

            eleven_labs_key = st.text_input(
                "ELEVEN LABS API KEY",
                type="password",
                value=get_api_key("ELEVEN LABS"),
                show_copy_button=True
            )
            show_eleven_key = st.button("Show")
            if show_eleven_key:
                eleven_labs_key = st.text_input(
                    "ELEVEN LABS API KEY",
                    value=get_api_key("ELEVEN LABS"),
                    show_copy_button=True
                )
            eleven_characters_remaining = st.text_input(
                "CHARACTERS REMAINING",
                value=getElevenRemaining(get_api_key("ELEVEN LABS")),
                disabled=True
            )

            automatic1111_url = st.text_input(
                "AUTOMATIC1111 URL",
                value=get_api_key("A1111"),
                show_copy_button=True
            )

    if st.button("Save"):
        # Implement saving logic here
        st.success("Keys Saved!")