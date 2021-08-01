import cv2
import numpy as np
from matplotlib import pyplot as plt 
from PIL import Image
import json
#data = json.load('bochum_000000_000313_gtFine_polygons.json')
bez_chashki = cv2.imread('bez_chashki.jpg',1)
s_chashkoi = cv2.imread('s_chashkoi.jpg',1)
plt.imshow(s_chashkoi)
plt.show()
imageCut=s_chashkoi[832:2000,123:1172]
plt.imshow(imageCut)
plt.show()
imageCut.shape
sko_maski0=np.std(imageCut[:,:,0])
sko_maski1=np.std(imageCut[:,:,1])
sko_maski2=np.std(imageCut[:,:,2])

sko_fona0=np.std(s_chashkoi[:,:,0])
sko_fona1=np.std(s_chashkoi[:,:,1])
sko_fona2=np.std(s_chashkoi[:,:,2])

result0=sko_maski0 / sko_fona0
result1=sko_maski1 / sko_fona1
result2=sko_maski2 / sko_fona2
print('СКО маски канала 0=',sko_maski0)
print('СКО маски канала 1=',sko_maski1)
print('СКО маски канала 2=',sko_maski2)

print('СКО фона канала 0=',sko_fona0)
print('СКО фона канала 1=',sko_fona1)
print('СКО фона канала 2=',sko_fona2)

print('Отношение СКО фон/маска канала 0=',result0)
print('Отношение СКО фон/маска канала 1=',result1)
print('Отношение СКО фон/маска канала 2=',result2)

