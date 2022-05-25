"""
@Time : 2022/5/25 18:35
@Author : sunny cao
@File : verification_code.py
"""
import pytesseract

from PIL import Image
image = Image.open("captcha.jpg")
print(image)
print(pytesseract.image_to_string(image))
