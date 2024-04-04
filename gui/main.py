import gradio as gr
from project_selection_ui import select_project_ui
from story_generation_ui import story_generation_ui
from gui.voice_generation_ui import voice_generation_ui
from gui.voice_generation_ui import elevenLabsUI
from gui.voice_generation_ui import elevenLabsUI2
# from gui.image_generation_ui import image_generation_ui
from compile_ui import create_compile_ui 
from config_ui import create_config_ui

ui_asset_dataframe = gr.Dataframe(interactive=False)

def run_app(colab=False):
    with gr.Blocks(css="footer {visibility: hidden}", title="Story Books" ) as UI:
        with gr.Row(variant='compact'):
            gr.HTML(f'''
                <div style="display: flex; justify-content: space-between; align-items: center; padding: 5px;">
                <h1 style="margin-left: 0px; font-size: 35px;">Story Books</h1>
                <div style="flex-grow: 1; text-align: right;">
                <h1></h1>
                </div>
                </div
            ''')
        project_selection = select_project_ui(UI)
        story_gen = story_generation_ui(UI)
        voice = elevenLabsUI2(UI)
        # voice_gen = voice_generation_ui(UI)
        # image_gen = image_generation_ui(UI)
        compile_video = create_compile_ui(UI)
        # config = create_config_ui(UI)
    # UI.launch(server_port=4000, height=1000, share=colab)
    UI.launch()
if __name__ == "__main__":
    run_app()