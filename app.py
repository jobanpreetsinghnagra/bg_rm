import gradio as gr
from PIL import Image

def background_remove(image_object):
    input_path = image_object
    output_path = 'output.png'
    input  = Image.open(input_path)
    output = remove(input)
    output.save(output_path)