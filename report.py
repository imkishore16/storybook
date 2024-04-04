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
file_list = list_files_in_folder(folder_path)

print(file_list)

# image_paths = ["/content/abouthem.jpg", "/content/abouthem.jpg"]
# texts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear', 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']
texts= [
    "Once upon a time, in the cozy town of Brightville, lived a curious boy named Timothy",
    "Timothy always dreamed of soaring through the sky in rockets",
    "His fascination with the twinkling stars inspired him every night",
    "One day, Timothy stumbled upon a dusty old book in the attic",
    "It was filled with pictures of rockets, planets, and astronauts",
    "Excitement danced in his eyes as he imagined his own space adventure",
    "Timothy's dream took flight when he built a cardboard rocket in his backyard",
    "With a vivid imagination and determination, he zoomed past the moon and landed on Mars",
    "There, he met a friendly alien named Zork who granted him three wishes",
    "Timothy wished for a rocket that could travel to every corner of the universe",
    "From that day forward, Timothy and Zork traveled together, exploring distant galaxies and meeting fascinating creatures",
    "Word of their incredible adventures spread, and kids from far and wide joined them",
    "Inspired by Timothy's dreams, they too built their own rockets and embarked on thrilling quests",
    "In Brightville, dreams became a reality, as the children learned that with imagination, anything is possible",
    "And so, Timothy's love for rockets continues to inspire generations, filling the world with wonder and boundless dreams"
]
output_pdf_path = "D:/Visual Studio 2019/StoryBlocks/gui/projects/new/output2.pdf"

create_pdf_with_images_and_text(file_list, texts, output_pdf_path)