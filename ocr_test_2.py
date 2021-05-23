import cv2
import pytesseract
import numpy as np
import requests

# 다운받을 이미지 url
url = "https://storage.googleapis.com/wm_timedata/time_image.jpg"

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)

image = cv2.imdecode(image_nparray, cv2.IMREAD_GRAYSCALE)
print(image.shape)
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(image, lang="kor", config=custom_config))
cv2.imshow('Image from url', image)
cv2.waitKey(0)
cv2.destroyAllWindow()
