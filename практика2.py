import cv2
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image
im = np.zeros((100,100,1))#задаю размер и канальность картинки
im[50,50] = (255) # выбираю середину и закрашиваю
#out= im.resize(size, resample=0, box=None)
blur1 = cv2.GaussianBlur(im,(5,5),0)
blur2 = cv2.GaussianBlur(im,(9,9),0)
blur3 = cv2.GaussianBlur(blur1,(5,5),0)

plt.subplot(121),plt.imshow(im),plt.title('Одноканальное изображение \n100 на 100')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur1),plt.title('сглаживание окном \nокном 5 на 5')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(im),plt.title('Одноканальное изображение \n100 на 100')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur2),plt.title('сглаживание окном \nокном 9 на 9')
plt.xticks([]), plt.yticks([])
plt.show()

plt.subplot(121),plt.imshow(im),plt.title('Одноканальное изображение \n100 на 100')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur3),plt.title('сглаживание окном \nокном 5 на 5 дважды')
plt.xticks([]), plt.yticks([])
plt.show()
