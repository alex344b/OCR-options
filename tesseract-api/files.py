from pdf import pdfText
from image import imageText
from threading import Thread

images = ["png", "jpeg", "jpg"]


def extractText(file):
    type = file.split('.')[1]
    if type == "pdf":
        pdfText(file)
    if type in images:
        imageText(file)


def background_task(file):
    reader_thread = Thread(target=extractText, args=(file,))
    reader_thread.start()
