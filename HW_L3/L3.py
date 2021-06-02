import cv2 as cv
import numpy as np

#Problem 1

img = cv.imread('Downloads/L3/practical_homework3/pic1.jpg') 
cv.imshow('pic1', img) 

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb) 

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#Problem 2

img = cv.imread('Downloads/L3/practical_homework3/pic1.jpg') 

cv.imshow('pic1', img) 

b, g, r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue(gray)', b)
cv.imshow('green(gray)', g)
cv.imshow('red(gray)', r)
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


#Problem 3

img = cv.imread('Downloads/L3/practical_homework3/pic2.jpg')
cv.imshow('pic2', img) 

average = cv.blur(img, (7,7)) 
cv.imshow('average blur', average)

bilateral1 = cv.bilateralFilter(img, 5, 15, 15)  
cv.imshow('bilateral', bilateral1)

#Second parameter controls treshold for edge gradient  
#In bilateral blure edges preserved but in average blur didn't


#Problem 4

img = cv.imread('Downloads/L3/practical_homework3/pic2.jpg')
cv.imshow('original image', img) 

blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 70, 255, -1)

masked_image = cv.bitwise_and(img, img, mask=mask)

cv.imshow('result', masked_image) 

#Problem 5

blank = np.zeros((500,500), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (100, 100), (400, 400), 128, -1)
circle = cv.circle(blank.copy(), (250, 250), 180, 128, -1)

xor_img = cv.bitwise_xor(rectangle, circle)
cv.imshow('xor', xor_img) 

or_img = cv.bitwise_or(rectangle, circle)
cv.imshow('or', or_img) 

pink = np.zeros((500,500,3), dtype = 'uint8')
pink[:] = (133, 21, 199)
b, g, r = cv.split(pink)

xor_b = cv.bitwise_and(xor_img, b)
xor_g = cv.bitwise_and(xor_img, g)
xor_r = cv.bitwise_and(xor_img, r)

merged = cv.merge([xor_b, xor_g, xor_r])
cv.imshow('merged image', merged)

cv.waitKey(0)