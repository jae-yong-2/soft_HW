import cv2 as cv  # OpenCV import
import numpy as np  # 행렬(img)를 만들기 위한 np import
import pyautogui as gui
import mouse
import time

table = 0
point = []
max_count=0

# 마우스 이벤트 콜백함수 정의
def mouse_callback(event, x, y, flags, param):
    global max_count
    if mouse.is_pressed("left"):
        point.append(gui.position())
        print(x,y)
        max_count=max_count+1
        print(max_count)
        time.sleep(0.1)


img = cv.imread('test1.PNG')  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)

table = int(input("테이블 수를 입력하세요. : "))
cv.namedWindow('image')  # 마우스 이벤트 영역 윈도우 생성
cv.setMouseCallback('image', mouse_callback)

def click_img():
    while (True):
        cv.imshow('image', img)
        if max_count==table:
            break
        k = cv.waitKey(1) & 0xFF
    cv.destroyAllWindows()

click_img()