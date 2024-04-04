# from openai import OpenAI
# import os
# import requests

# # client = OpenAI(api_key="")

# # prompts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear']#, 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']
# # output_folder = "/gui/projects/new/images"

# # for i, prompt in enumerate(prompts):
# #     print("prompt  " , prompt)
# # for i, prompt in enumerate(prompts):
# #     print("prompt  " , prompt)
# #     response = client.images.generate(
# #         model="dall-e-3",
# #         prompt=prompt,
# #         size="1024x1024",
# #         quality="standard",
# #         n=1,
# #     )

# #     if response.status_code == 200:
# #         image_url = response.data[0].url
# #         filename = os.path.join(output_folder, f"image_{i}.jpg")  
# #         response = requests.get(image_url)

# #         if response.status_code == 200:
# #             with open(filename, 'wb') as f:
# #                 f.write(response.content)
# #             print("Image downloaded successfully as:", filename)
# #         else:
# #             print("Failed to download image. Status code:", response)
# #     else:
# #         print("Failed to generate image. Status code:", response)


# # # import os
# # # import requests

# # # api_key = ''

# # # prompts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear']#, 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']


# # # # Define the directory to store the downloaded images
# # # output_directory = "downloaded_images"

# # # # Create the output directory if it doesn't exist
# # # os.makedirs(output_directory, exist_ok=True)

# # # # Iterate over each prompt
# # # for i, prompt in enumerate(prompts, start=1):
# # #     # Initialize the OpenAI client
# # #     client = Client(api_key=api_key)

# # #     # Make a request to generate an image
# # #     response = client.images.generate(
# # #         model="dall-e-3",
# # #         prompt=prompt,
# # #         size="1024x1024",
# # #         quality="standard",
# # #         n=1,
# # #     )

# # #     # Extract the image URL from the response
# # #     image_url = response.data[0].url

# # #     # Define the filename to save the image
# # #     filename = os.path.join(output_directory, f"image_{i}.png")

# # #     # Send a GET request to the image URL
# # #     image_response = requests.get(image_url)

# # #     # Check if the request was successful (status code 200)
# # #     if image_response.status_code == 200:
# # #         # Open a file in binary write mode and write the content of the response to it
# # #         with open(filename, 'wb') as f:
# # #             f.write(image_response.content)
# # #         print(f"Image downloaded successfully as: {filename}")
# # #     else:
# # #         print(f"Failed to download image for prompt '{prompt}'. Status code: {image_response.status_code}")


# import os
# import requests
# from openai import Client
# # Replace 'YOUR_API_KEY' with your actual DALL-E API key
# # api_key = 'YOUR_API_KEY'
# api_key = ''

# # Define the list of prompts
# prompts = ['In a city plagued by darkness and despair, Batman and Superman stood on opposite sides', 'of justice. Batman, the Dark Knight, relied on his gadgets and stealth to strike fear']#, 'into the hearts of criminals. Superman, the Man of Steel, possessed incredible strength and speed,', 'using his powers to protect the innocent. Their paths crossed when an ancient artifact, rumored', 'to grant ultimate power, arose. Both heroes sought to possess it, believing it would enable', 'them to rid the world of evil. A fierce battle ensued, each unleashing their full', 'might upon the other. But as the dust settled, they realized their quest for power', 'had blinded them. They recognized that true strength lay not in dominance, but in unity.', 'Understanding this, they joined forces as a new alliance, working together to protect the city', 'from impending doom. With their combined strengths, Batman and Superman became an unstoppable force, restoring', 'hope and justice to their once desolate city. And in their unity, they discovered that', 'the greatest heroes are not defined by their powers, but by the choices they make', 'to protect and save the lives of others.']


# # Define the directory to store the downloaded images
# output_directory = "downloaded_images"

# # Create the output directory if it doesn't exist
# os.makedirs(output_directory, exist_ok=True)

# # Iterate over each prompt
# for i, prompt in enumerate(prompts, start=1):
#     # Initialize the OpenAI client
#     client = Client(api_key=api_key)

#     # Make a request to generate an image
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )

#     # Extract the image URL from the response
#     image_url = response.data[0].url

#     # Define the filename to save the image
#     filename = os.path.join(output_directory, f"image_{i}.png")

#     # Send a GET request to the image URL
#     image_response = requests.get(image_url)

#     # Check if the request was successful (status code 200)
#     if image_response.status_code == 200:
#         # Open a file in binary write mode and write the content of the response to it
#         with open(filename, 'wb') as f:
#             f.write(image_response.content)
#         print(f"Image downloaded successfully as: {filename}")
#     else:
#         print(f"Failed to download image for prompt '{prompt}'. Status code: {image_response.status_code}")



import torch
from diffusers import StableCascadeDecoderPipeline, StableCascadePriorPipeline
# // acclerate, transformer
prompt = "Batman fights superman , hand to hand combat"
negative_prompt = ""

prior = StableCascadePriorPipeline.from_pretrained("stabilityai/stable-cascade-prior", variant="bf16", torch_dtype=torch.bfloat16)
decoder = StableCascadeDecoderPipeline.from_pretrained("stabilityai/stable-cascade", variant="bf16", torch_dtype=torch.float16)

prior.enable_model_cpu_offload()
prior_output = prior(
    prompt=prompt,
    height=1024,
    width=1024,
    negative_prompt=negative_prompt,
    guidance_scale=4.0,
    num_images_per_prompt=1,
    num_inference_steps=20
)

decoder.enable_model_cpu_offload()
decoder_output = decoder(
    image_embeddings=prior_output.image_embeddings.to(torch.float16),
    prompt=prompt,
    negative_prompt=negative_prompt,
    guidance_scale=0.0,
    output_type="pil",
    num_inference_steps=10
).images[0]
decoder_output.save("D:/Visual Studio 2019/StoryBlocks/pycascade.png")
