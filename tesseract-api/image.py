from pytesseract import image_to_string
from db import insertText
from PIL import Image


def imageText(file, lang='spa'):
    context = image_to_string(Image.open('./files/'+file), lang=lang)
    insertText(file, context)
