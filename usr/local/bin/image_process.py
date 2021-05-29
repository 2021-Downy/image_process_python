import cv2
import pytesseract
import numpy as np
import requests
import update_time

# 다운받을 이미지 url
url = "https://storage.googleapis.com/wm_timedata/time_image.jpg"

image_nparray = np.asarray(bytearray(requests.get(url).content), dtype=np.uint8)

image = cv2.imdecode(image_nparray, cv2.IMREAD_GRAYSCALE)
print(image.shape)
custom_config = r'--oem 3 --psm 6'
ext_txt = pytesseract.image_to_string(image, lang="kor", config=custom_config)
print(ext_txt)

# cv2.imshow('Image from url', image)
# cv2.waitKey(0)
# cv2.destroyAllWindow()

# 1번 세탁기로 임의지정. TODO : 모든 세탁기에 적용 수행
update_time.update_db(1,ext_txt)