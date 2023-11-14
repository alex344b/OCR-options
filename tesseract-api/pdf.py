from db import insertText
import PyPDF2


def pdfText(pdf):
    context = ""
    reader = PyPDF2.PdfReader('./files/'+pdf)
    for page in reader.pages:
        context += page.extract_text() + "------"
    insertText(pdf, context)
    return
