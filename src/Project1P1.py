####################################
#CSE473 Project 1 Problem 1
#Author: Jeremy Caldwell (jcaldwel)
#
####################################

## Part a ##
import numpy as np
import cv2
#read in image
img = cv2.imread('C:\Users\Jeremy\Homework\CSE473\Python\lena_gray.jpg', 0)

#create kernel filters
xSob = np.array([(-1,0,1),(-2,0,2),(-1,0,1)])
ySob = np.array([(-1,-2,-1),(0,0,0),(1,2,1)])

#create array to hold filtered image
xSobImg = np.zeros((512,512))
ySobImg = np.zeros((512,512))
sobImg = np.zeros((512,512))

# pad image so that every original pixel has 8 neighbors for convolution with kernel filter
img = np.pad(img,(1,1),'edge')

#perform convolution with Sobel filters
#note: the x Sobel filtered image, the y Sobel filtered image, and the overall Sobel filtered image are calculated at the same time to save repeated steps of moving the filters
for row in range(1,img.shape[0]-1):
    for col in range(1,img.shape[1]-1):        
        #note: parts of the image multiplied by the 0 portions of the filters
        xSum = (xSob.item(0,0) * img.item(row-1,col-1)) + (xSob.item(0,2) * img.item(row-1,col+1)) + (xSob.item(1,0) * img.item(row,col-1)) + (xSob.item(1,2) * img.item(row,col+1)) + (xSob.item(2,0) * img.item(row+1,col-1)) + (xSob.item(2,2) * img.item(row+1,col+1))
        ySum = (ySob.item(0,0) * img.item(row-1,col-1)) + (ySob.item(0,1) * img.item(row-1,col)) + (ySob.item(0,2) * img.item(row-1,col+1)) + (ySob.item(2,0) * img.item(row+1,col-1)) + (ySob.item(2,1) * img.item(row+1,col)) + (ySob.item(2,2) * img.item(row+1,col+1))
        xSobImg.itemset((row-1,col-1),xSum)
        ySobImg.itemset((row-1,col-1),ySum)
        sobImg.itemset((row-1,col-1),np.sqrt(xSum**2 + ySum**2))
        
cv2.imwrite('xSob.jpg',xSobImg) 
cv2.imwrite('ySob.jpg',ySobImg)
cv2.imwrite('sob.jpg',sobImg)

### Part b ###

#create kernel filters
xSob1 = np.array([1,2,1])[:,None]
xSob2 = np.array([-1,0,1])[None,:]

ySob1 = np.array([-1,0,1])[:,None]
ySob2 = np.array([1,2,1])[None,:]

#create array to hold filtered image
xSobImg2 = np.zeros((512,512))
ySobImg2 = np.zeros((512,512))

#perform convolution with first 1d Sobel filters
for row in range(1,img.shape[0]-1):
    for col in range(1,img.shape[1]-1):
        xSum = xSob1.item(0,0) * img.item(row-1,col) + xSob1.item(1,0) * img.item(row,col) + xSob1.item(2,0) * img.item(row+1,col)
        ySum = ySob1.item(0,0) * img.item(row-1,col) + ySob1.item(1,0) * img.item(row,col) + ySob1.item(2,0) * img.item(row+1,col)
        xSobImg2.itemset((row-1,col-1),xSum)
        ySobImg2.itemset((row-1,col-1),ySum)

#pad once-convoluted images so they can be convolved again in the other dimension
xSobImg2Pad = np.pad(xSobImg2,(1,1),'edge')
ySobImg2Pad = np.pad(ySobImg2,(1,1),'edge')

#perform convolution with second 1d Sobel filters
for row in range(1,xSobImg2Pad.shape[0]-1):
    for col in range(1,xSobImg2Pad.shape[1]-1):
        xSum = xSob2.item(0,0) * xSobImg2Pad.item(row,col-1) + xSob2.item(0,1) * xSobImg2Pad.item(row,col) + xSob2.item(0,2) * xSobImg2Pad.item(row,col+1)
        ySum = ySob2.item(0,0) * ySobImg2Pad.item(row,col-1) + ySob2.item(0,1) * ySobImg2Pad.item(row,col) + ySob2.item(0,2) * ySobImg2Pad.item(row,col+1)
        xSobImg2.itemset((row-1,col-1),xSum)
        ySobImg2.itemset((row-1,col-1),ySum)
                
cv2.imwrite('xSobSep.jpg',xSobImg2) 
cv2.imwrite('ySobSep.jpg',ySobImg2)

if(xSobImg == xSobImg2).all():
    print 'x same'
else:
    print 'x different'

if(ySobImg == ySobImg2).all():
    print 'y same'
else:
    print 'y different'
