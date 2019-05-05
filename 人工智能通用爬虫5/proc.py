from PIL import Image

import pytesseract

file_path = "E:\pycharmcode\pachong\人工智能通用爬虫5\\1.jpg"

img = Image.open(file_path)

print(pytesseract.image_to_string(img))