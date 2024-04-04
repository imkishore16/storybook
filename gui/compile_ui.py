import gradio as gr
import json
import os
import requests
import ast
from openai import Client

api_key = ''

path_to_json = "D:/Visual Studio 2019/StoryBlocks/gui/projects/new/content.json"

def load_json_data(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return None, None

    try:
        # Load JSON data from the file
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            print("datadatadatadatadatadatadatadatadatadatadatadatadatadatadatadatadatadatadata")
            print(data)
            # Extract the word list from the JSON data
            word_list = data.get('word_lists', [])
            print("word_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_listword_list")
            print(word_list)
            return data, word_list
    except Exception as e:
        print(f"Error: Failed to load JSON data from '{path}'. {e}")
        return None, None
# Example usage:
json_data, prompts = load_json_data(path_to_json)







# Define the list of prompts
# prompts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear']#, 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']


# Define the directory to store the downloaded images


def create_images(prompts_list):
    
    output_directory = "D:/Visual Studio 2019/StoryBlocks/gui/projects/new/images"
    os.makedirs(output_directory, exist_ok=True)
    print("#########################################################")

    for i, prompt in enumerate(prompts_list, start=1):
        client = Client(api_key=api_key)
        # Make a request to generate an image
        print("dalle prompt  : " ,prompt)
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        # Extract the image URL from the response
        image_url = response.data[0].url

        # Define the filename to save the image
        filename = os.path.join(output_directory, f"image_{i}.png")

        # Send a GET request to the image URL
        image_response = requests.get(image_url)

        # Check if the request was successful (status code 200)
        if image_response.status_code == 200:
            # Open a file in binary write mode and write the content of the response to it
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            print(f"Image downloaded successfully as: {filename}")
        else:
            print(f"Failed to download image for prompt '{prompt}'. Status code: {image_response.status_code}")




from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

def split_text(text, max_line_length):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) + 1 <= max_line_length:
            current_line += ' ' + word if current_line else word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def list_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        raise ValueError("The specified folder path does not exist.")
    files = os.listdir(folder_path)
    files = [os.path.join(folder_path, file) for file in files if os.path.isfile(os.path.join(folder_path, file))]
    return files


def create_pdf_with_images_and_text(image_paths, texts, output_path):
    # Create a canvas object
    c = canvas.Canvas(output_path, pagesize=letter)

    # Get the width and height of the page
    page_width, page_height = letter

    # Calculate text box size and position
    text_width = 0.85 * page_width  # 85% of page width
    text_height = 0.4 * page_height  # 40% of page height
    text_x = (page_width - text_width) / 2
    text_y = 50  # Adjust this value based on your preference

    for image_path, text in zip(image_paths, texts):
        # Add image to the PDF (top 50% with 5% space at top)
        img_width = 300
        img_height = 300
        img_x = (page_width - img_width) / 2
        img_y = page_height - 100 - img_height
        img = ImageReader(image_path)
        c.drawImage(img, img_x, img_y, width=img_width, height=img_height)

        # Split text into lines
        max_line_length = int(text_width / 8)  # approximate character width
        lines = split_text(text, max_line_length)

        # Draw text line by line
        c.setFont("Helvetica", 12)
        y_offset = text_y + text_height - 12  # Starting y-coordinate
        for line in lines:
            c.drawCentredString(text_x + text_width / 2, y_offset, line)
            y_offset -= 16  # Adjust as needed to control line spacing

        # Add a new page
        c.showPage()

    print("Save the PDF")
    c.save()




folder_path='D:/Visual Studio 2019/StoryBlocks/gui/projects/new/images'
# print(file_list)
image_paths=list_files_in_folder(folder_path)
# image_paths = ["/content/abouthem.jpg", "/content/abouthem.jpg"]
# texts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear', 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']
output_pdf_path = "D:/Visual Studio 2019/StoryBlocks/gui/projects/new/output.pdf"

json_data, prompts
file_list=""

def execute():
    json_data, prompts_list = load_json_data(path_to_json)
    # print("execute funtion")
    # print(prompts_list)
    prompts_list=ast.literal_eval(ast.literal_eval(prompts_list))
    create_images(prompts_list)
    create_pdf_with_images_and_text(image_paths, prompts_list, output_pdf_path)


def create_compile_ui(Blocks):
    with gr.Tab("Compile Video") as compile_ui:
        with gr.Column():
            with gr.Row():
                gr.Markdown("## Compile Video")
                # Add a button to call a function when clicked
                compile_button = gr.Button("Compile", size="sm", interactive=True, visible=True)
                compile_button.click(execute)
    return compile_ui