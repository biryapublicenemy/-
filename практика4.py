import cv2
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image
src1 = cv2.imread('1.jpg',1)
src2 = cv2.imread('2.jpg',1)
diff12= src2-src1 
plt.imshow(diff12),plt.title('Результат пункта а ')
plt.show()
#пункт б
kernel = np.ones((11, 11),dtype = np.float32)
cleandiff_erode = cv2.erode(diff12,kernel,iterations=1)
plt.imshow(cleandiff_erode),plt.title('Eroded image ')
plt.show()

cleandiff_dilate = cv2.dilate(cleandiff_erode,kernel,iterations=1)
plt.imshow(cleandiff_dilate),plt.title('Dilated image ')
plt.show()
#пункт с 
dirtydiff_dilate = cv2.dilate(diff12,kernel,iterations=1)
plt.imshow(dirtydiff_dilate),plt.title('Dilated image пункт с')
plt.show()

dirtydiff_erode = cv2.erode(dirtydiff_dilate,kernel,iterations=1)
plt.imshow(dirtydiff_erode),plt.title('Eroded image пункт с')
plt.show()
#функция dilate выполняет расширение пикселей первого плана(чаще всего белые), из-за этого области белых пикселей увеличиваются
#при эрозии пиксель считается 1 если все пиксели в ядре равны 1, иначе он разрушается, таким образом, размер объекта переднего плана уменьшается или уменьшается белая область на изображении
