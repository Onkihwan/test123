import cv2

# OpenCV 버전 출력
print("OpenCV version:", cv2.__version__)

# 간단한 이미지 생성 및 저장
import numpy as np

# 검은색 이미지 생성
img = np.zeros((100, 100, 3), dtype=np.uint8)

# 흰색 사각형 그리기

cv2.rectangle(img, (20, 20), (80, 80), (255, 255, 255), -1)

# 이미지 저장
cv2.imwrite('test_image.png', img)

print("Test image saved as 'test_image.png'")

