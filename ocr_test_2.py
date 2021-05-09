import cv2
import pytesseract

img = cv2.imread('example4.png',cv2.IMREAD_GRAYSCALE)

# Adding custom options
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, lang="kor", config=custom_config))
