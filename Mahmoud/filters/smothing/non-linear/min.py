#########################################
## Name:  Mahmoud Ahmed Zaytoni     #####
## Id:    2021425                   #####
## Group: G5                        #####
## assignment:  3                   #####
#########################################
import cv2 as cv
import numpy as np

def apply_min_filter(img, mask_size):
    rows, cols, channels = img.shape
    output = np.zeros((rows, cols, channels), dtype=np.uint8)
    
    border_size = mask_size // 2
    
    # Pad the input image with REPLICATE to handle borders
    padded_img = cv.copyMakeBorder(img, border_size, border_size, border_size, border_size,cv.BORDER_REPLICATE)
    
    for i in range(border_size, rows + border_size):
        for j in range(border_size, cols + border_size):
            # Get the neighborhood of the current pixel
            neighborhood = padded_img[i-border_size:i+border_size+1, j-border_size:j+border_size+1]
            
            # Calculate the Min of the neighborhood along the third axis (channels)
            mn = np.min(neighborhood, axis=(0,1))
            output[i - border_size, j - border_size] = mn
    return output
org = cv.imread('org.jpg')
cv.imshow('original', org)
cv.waitKey(0)

out = apply_min_filter(org, 3)
cv.imshow('modified', out)
cv.waitKey(0)