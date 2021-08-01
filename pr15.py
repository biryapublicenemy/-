import cv2 
import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as img
def graphs(x):
	plt.imshow(x)
	plt.show()
	
im = img.imread('boris.jpg')

kernel1 = np.array([[0,0,-1,2,-1],[0,-1,2,-1,0],[0,-1,2,-1,0],[-1,2,-1,0,0],[2,-1,0,0,0]])
#ad=cv2.getGaussianKernel( 5, 3 )

ad=cv2.filter2D( im,-1, kernel1 )

graphs(ad)

graphs(im)


#cv2.imwrite ('Q113.jpg', im)
#cv2.imwrite ('Q213.jpg', ad)
