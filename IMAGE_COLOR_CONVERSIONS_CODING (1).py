

# import cv2
# from google.colab.patches import cv2.


#1.	Read and Display an Image
import cv2 
image=cv2.imread('image.jpg',1)
image =cv2.resize(image, (506, 317))
cv2.imshow('WINDOW',image)
cv2.waitKey(0)
cv2.destroyAllWindows()



#2.	Draw Shapes and Add Text
import cv2
image = cv2.imread("image.jpg")
image = cv2.resize(image, (506, 317))
res = cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (255,0,0), 10)
cv2.imshow('WINDOW', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


#3.Image Color Conversion

import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(300,200))
cv2.imshow('ORIGINAL IMAGE',image)
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()


#4.Access and Manipulate Image Pixels
pixel_value = image[100, 100]
print(f"Pixel value at (100, 100): {pixel_value}")

import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(400,300))
cv2.imshow('ORIGINAL IMAGE',image)
image[200, 200] = [255, 255, 255] 
cv2.imshow('MODIFIED IMAGE', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#5.Image Resizing
cv2.imshow('ORIGINAL IMAGE',image)
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
cv2.imshow('RESIZED IMAGE', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#6.	Image Cropping
Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.

import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(400,300))
x, y = 50, 50
width, height = 100, 100
roi = image[y:y + height, x:x + width]
cv2.imshow('CROPPED IMAGE', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

#7.Image Flipping
import cv2
image = cv2.imread("forest.png")
image = cv2.resize(image,(300,200))
res=cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('ORIGINAL IMAGE',image)
cv2.imshow('FLIPPED IMAGE', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#8.Write and Save the Modified Image
import cv2
img = cv2.imread("forest.png")
img = cv2.resize(img,(300,200))
cv2.imwrite('boat_pic.jpg',img)
