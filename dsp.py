import cv2 
import numpy as np
import sys
import matplotlib.pyplot as plt

import matplotlib.image as img
image = cv2.imread('king.jpeg')
#b, g, r = cv2.split(image)
#cv2.imshow('blue', b)
#cv2.imshow('green', g)
#cv2.imshow('red', r)cv2.waitKey(0)

# параметры цветового фильтра
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 245, 255), np.uint8)
hsv = cv2.cvtColor( image, cv2.COLOR_BGR2HSV ) # меняем цветовую модель с BGR на HSV 
thresh = cv2.inRange( hsv, hsv_min, hsv_max ) # применяем цветовой фильтр
plt.imshow(thresh)
plt.show()
# ищем контуры и складируем их в переменную contours
contours, hierarchy = cv2.findContours( thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )
# отображаем контуры поверх изображения
cv2.drawContours( image, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
cv2.imshow('contours', image) # выводим итоговое изображение в окно
index = 0
layer = 0

def update():
        vis = image.copy()
        cv2.drawContours( vis, contours, index, (255,0,0), 2, cv2.LINE_AA, hierarchy, layer )
        cv2.imshow('contours', vis)

def update_index(v):
        global index
        index = v-1
        update()

def update_layer(v):
        global layer
        layer = v
        update()
        update_index(0)
        update_layer(0)
cv2.createTrackbar( "contour", "contours", 0, 7, update_index )
cv2.createTrackbar( "layers", "contours", 0, 7, update_layer )
cv2.waitKey()
cv2.destroyAllWindows()
