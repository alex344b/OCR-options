from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_file = "image/bill.jpg"
img = Image.open(img_file)
ocr_result = pytesseract.image_to_string(img)
print(ocr_result)