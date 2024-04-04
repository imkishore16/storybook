# import os
# import json
# import pyttsx3
# import gradio as gr
# from config.api_db import get_api_key
# from api_utils.eleven import getVoices, generateVoice
# from config.project_db import get_project_name, set_project_name


# def getElevenlabsVoices():
#     # api_key = get_api_key("ELEVEN LABS")
#     api_key ="e6b964fdf54c670d55239f37dc2bc236"
#     voices = list(reversed(getVoices(api_key).keys()))
#     return voices
# voiceChoice = gr.Radio(getElevenlabsVoices(), label="Elevenlabs voice", value="Antoni", interactive=True)

# def generateVoice_ElevenLabs(selected_voice):
#   current_selected_project = get_project_name()
  
#   with open(f"projects/{current_selected_project}/content.json", "r") as f:
#     content = json.load(f)
#     story = content["content"]
#   generateVoice(story,selected_voice ,current_selected_project , api_key="e6b964fdf54c670d55239f37dc2bc236")
#   return  gr.update(value=f"projects/{current_selected_project}/audio.mp3")

# def generateVoice_PythonTTS():
#   current_selected_project = get_project_name()  
#   with open(f"projects/{current_selected_project}/content.json", "r") as f:
#     content = json.load(f)
#     story = content["content"]
#   print(story)
#   engine = pyttsx3.init()
#   engine.save_to_file(story, f"projects/{current_selected_project}/audio.mp3")
#   engine.runAndWait()
#   return  gr.update(value=f"projects/{current_selected_project}/audio.mp3")


# def elevenLabsUI(UI: gr.Blocks):
#   with gr.Row(visible=False) as eleven_labs_ui:
#     with gr.Column():
#       gr.Markdown("## Elevenlabs Voice")
#       voiceChoice.render()
#       elevenlab_generate_button = gr.Button("Generate Voice", size="sm", interactive=True, visible=True)
#       generated_audio = gr.Audio(label="Audio", interactive=True, visible=False)
#       elevenlab_generate_button.click(lambda : gr.update(visible=True), outputs=[generated_audio]).success(generateVoice_ElevenLabs ,inputs=[voiceChoice] , outputs=[generated_audio])
#   return eleven_labs_ui

# def pythonTTSUI(UI: gr.Blocks):
#   with gr.Row(visible=False) as python_tts_ui:
#     with gr.Column():
#       gr.Markdown("## Python TTS")
#       pyttsx3_generate_button = gr.Button("Generate Voice", size="sm", interactive=True, visible=True)
#       generated_audio = gr.Audio(label="Audio", interactive=True, visible=False)
#       pyttsx3_generate_button.click(lambda : gr.update(visible=True), outputs=[generated_audio]).success(generateVoice_PythonTTS , outputs=[generated_audio])
#   return python_tts_ui
    

# def voice_generation_ui(UI: gr.Blocks):
#   with gr.Tab("Voice Generation") as voice_generation:
#     gr.Markdown("## Generate Voice")
#     choice_TTS = gr.Radio([ 'Python TTS', 'ElevenLabs'], label="Choose an voice generator")
#     eleven_labs_ui = elevenLabsUI(UI) 
#     python_tts_ui = pythonTTSUI(UI)
#     choice_TTS.change(lambda x: (gr.update(visible= x == choice_TTS.choices[1]), gr.update(visible= x == choice_TTS.choices[0])), [choice_TTS], [eleven_labs_ui, python_tts_ui]) # type: ignore
#   return voice_generation


import os
import json
import pyttsx3
import gradio as gr
from config.api_db import get_api_key
from api_utils.eleven import getVoices, generateVoice
from config.project_db import get_project_name, set_project_name


def getElevenlabsVoices():
    api_key ="e6b964fdf54c670d55239f37dc2bc236"
    voices = list(reversed(getVoices(api_key).keys()))
    return voices

voiceChoice = gr.Radio(getElevenlabsVoices(), label="Elevenlabs voice", value="Antoni", interactive=True)

def generateVoice_ElevenLabs(selected_voice):
    current_selected_project = get_project_name()
  
    with open(f"projects/{current_selected_project}/content.json", "r") as f:
        content = json.load(f)
        story = content["content"]
    api_key ="e6b964fdf54c670d55239f37dc2bc236" 
    generateVoice(story, selected_voice, current_selected_project, api_key=api_key)
    return f"projects/{current_selected_project}/audio.mp3"

def generateVoice_PythonTTS():
    current_selected_project = get_project_name()  
    with open(f"projects/{current_selected_project}/content.json", "r") as f:
        content = json.load(f)
        story = content["content"]
    engine = pyttsx3.init()
    engine.save_to_file(story, f"projects/{current_selected_project}/audio.mp3")
    engine.runAndWait()
    return f"projects/{current_selected_project}/audio.mp3"


def elevenLabsUI(UI):
    with gr.Row(visible=True) as eleven_labs_ui:
        with gr.Column():
            gr.Markdown("## Elevenlabs Voice")
            voiceChoice.render()
            elevenlab_generate_button = gr.Button("Generate Voice", size="sm", interactive=True, visible=True)
            generated_audio = gr.Audio(label="Audio", interactive=True, visible=False)
            elevenlab_generate_button.click(lambda: gr.update(visible=True), outputs=[generated_audio]).success(generateVoice_ElevenLabs, inputs=[voiceChoice], outputs=[generated_audio])
    return eleven_labs_ui

def pythonTTSUI(UI):
    with gr.Row(visible=False) as python_tts_ui:
        with gr.Column():
            gr.Markdown("## Python TTS")
            pyttsx3_generate_button = gr.Button("Generate Voice", size="sm", interactive=True, visible=True)
            generated_audio = gr.Audio(label="Audio", interactive=True, visible=False)
            pyttsx3_generate_button.click(lambda: gr.update(visible=True), outputs=[generated_audio]).success(generateVoice_PythonTTS, outputs=[generated_audio])
    return python_tts_ui
    

# def voice_generation_ui(UI):
#     with gr.Tab("Voice Generation") as voice_generation:
#         gr.Markdown("## Generate Voice")
#         choice_TTS = gr.Radio(['Python TTS', 'ElevenLabs'], label="Choose a voice generator")
#         eleven_labs_ui = elevenLabsUI(UI) 
#         python_tts_ui = pythonTTSUI(UI)
#         elevenLabsUI(UI)
#         choice_TTS.change(lambda x: (gr.update(visible= x == choice_TTS.choices[1]), gr.update(visible= x == choice_TTS.choices[0])), [choice_TTS], [eleven_labs_ui, python_tts_ui]) # type: ignore
#     # return voice_generation
#     return voice_generation


def voice_generation_ui(UI):
    with gr.Tab("Voice Generation") as voice_generation:

      gr.Markdown("## Generate Voice")
      gr.Markdown("### Choose a voice generator")
      with gr.Row(visible=True):
        with gr.Column(visible=False) as story_generation_column:
          elevenLabsUI(UI)

    return voice_generation

def elevenLabsUI2(UI):
    with gr.Tab("Voice Generation") as voice_generation:
        with gr.Row(visible=True) as eleven_labs_ui:
            with gr.Column():
                gr.Markdown("## Elevenlabs Voice")
                voiceChoice.render()
                elevenlab_generate_button = gr.Button("Generate Voice", size="sm", interactive=True, visible=True)
                generated_audio = gr.Audio(label="Audio", interactive=True, visible=False)
                elevenlab_generate_button.click(lambda: gr.update(visible=True), outputs=[generated_audio]).success(generateVoice_ElevenLabs, inputs=[voiceChoice], outputs=[generated_audio])
    return eleven_labs_ui
