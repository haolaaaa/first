import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"
image = Image.open("a.png")
text = pytesseract.image_to_string(image)
print(text)