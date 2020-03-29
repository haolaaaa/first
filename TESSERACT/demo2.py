import pytesseract
from PIL import Image
from urllib import request
import time
def main():
    pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract\tesseract.exe"
    url = 'https://www.58pic.com/index.php?m=userinfo&a=getImgCaptch&v=1585191488656'
    while True:
        request.urlretrieve(url,'captcha.png')
        image = Image.open('captcha.png')
        text = pytesseract.image_to_string(image)
        print(text)
        # time.sleep(2)

if __name__ == '__main__':
    main()
    