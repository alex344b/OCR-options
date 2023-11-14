from PIL import Image
from pytesseract import image_to_string
from pdf2image import convert_from_bytes
import PyPDF2
import os


texts = {}


def imageText(image, lang='eng'):
    return image_to_string(Image.open(image), lang=lang)


def pdfText(pdf):
    reader = PyPDF2.PdfReader(pdf)
    for page in reader.pages:
        print(page.extract_text())


def pdfToImage(pdf):
    with open(pdf, "rb") as pdf:
        pages = convert_from_bytes(pdf.read())
        pageNr = 0
        for page in pages:
            pageNr += 1
            fileName = "page_" + str(pageNr) + ".jpg"
            page.save(fileName, format="jpeg")


def imagePath():
    for dirpath, dirnames, files in os.walk('./images'):
        for file in files:
            texts[file.split('.')[0]] = imageText('./images/' + file, 'spa')


def writeToFile():
    save = open('text.json', 'w')
    save.write(str(texts))
    save.close()


# print(imageText("test.jpg"))
# pdfToImage("test.pdf")
# print(imageText("page_1.jpg", 'spa'))
# print(imageText("test.png"))
# pdfText("test.pdf")

imagePath()
writeToFile()
