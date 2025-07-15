import gradio as gr
from PIL import Image
from rembg import remove


def background_remove(inp: Image.Image) -> Image.Image:
    output = remove(inp)
    return output  

interface = gr.Interface(
    fn=background_remove,
    inputs=gr.Image(type='pil'),
    outputs=gr.Image(type='pil'),
    title='Background Remover'
)

interface.launch()