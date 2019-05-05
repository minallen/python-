


import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\anzhuang\Tesseract-OCR\tesseract.exe"


image = Image.open('d.png')

#text = pytesseract.image_to_string(image)
text = pytesseract.image_to_string(image,lang='chi_sim')
print(text)


