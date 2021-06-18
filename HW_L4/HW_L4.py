import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#Problem 1

img = cv.imread('pic1.jpg') 
 
cv.imshow('pic1', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(256)
plt.plot(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


plt.show()

cv.waitKey(0)

# Problem 2

img = cv.imread('pic1.jpg') 

cv.imshow('pic1', img) 

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256]) 
    mpl.use('tkagg') #backend for using matplotlib with any shell
    x = np.arange(256)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')


plt.show()

cv.waitKey(0)

#Problem 3

img = cv.imread('pic1.jpg') 
cv.imshow('pic1', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# by hand
threshold, thresh = cv.threshold(gray, 80, 255, cv.THRESH_BINARY) 
cv.imshow('threshold by hand', thresh) 

# adaptive with mean
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold with mean', adaptive_thresh) 

# adaptive with gaussian

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)

#Problem 4
img = cv.imread('pic2.jpg') 
cv.imshow('pic2', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)  #matrix value type float 64
lap = np.uint8(np.absolute(lap))

cv.imshow('laplacian', lap) 


canny = cv.Canny(gray, 200, 220)

cv.imshow('canny', canny) 

cv.waitKey(0)
