# # txt파일로 저장
#
# from PIL import Image
# import cv2
# import pytesseract
# from pytesseract import image_to_string
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# filename = "example3.png"
# image = Image.open(filename)
# text = image_to_string(image, lang="kor")
#
# with open("sampleG2.txt", "w") as f:
#     f.write(text)
