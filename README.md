# COLOR_CONVERSIONS_OF-IMAGE
## AIM
Write a Python program using OpenCV that performs the following tasks:

i) Read and Display an Image.

ii) 	Draw Shapes and Add Text.

iii) Image Color Conversion.

iv) Access and Manipulate Image Pixels.

v) Image Resizing

vi) Image Cropping

vii) Image Flipping

viii)	Write and Save the Modified Image


## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Load an image from your local directory and display it.
### Step2:
o	Draw a line from the top-left to the bottom-right of the image.
o	Draw a circle at the center of the image.
o	Draw a rectangle around a specific region of interest in the image.
o	Add the text "OpenCV Drawing" at the top-left corner of the image.

### Step3:
o	Convert the image from RGB to HSV and display it.
o	Convert the image from RGB to GRAY and display it.
o	Convert the image from RGB to YCrCb and display it.
o	Convert the HSV image back to RGB and display it.

### Step4:
o	Access and print the value of the pixel at coordinates (100, 100).
o	Modify the color of the pixel at (200, 200) to white.

### Step5:
o	Resize the original image to half its size and display it.
### Step6:
o	Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.
### Step7:
o	Flip the original image horizontally and display it.
o	Flip the original image vertically and display it.

### Step8:
o	Save the final modified image to your local directory.



### Developed By:Nivetha A
### Register Number:212222230101


#### Program & Output::

### i)Read and Display an Image
Load an image from your local directory and display it
```
import cv2 
image=cv2.imread('image.jpg',1)
image =cv2.resize(image, (506, 317))
cv2.imshow('WINDOW',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/ba318b2c-45ba-48ad-b006-5bd77cf9a294)


### ii)Draw Shapes and Add Text
(1) Draw a line from the top-left to the bottom-right of the image.
```
import cv2
image = cv2.imread("image.jpg")
image = cv2.resize(image, (506, 317))
res = cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (255,0,0), 10)
cv2.imshow('WINDOW', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/9a07c487-e61b-431e-9266-3842262b9f86)

(2) Draw a circle at the center of the image.

```
import cv2
image = cv2.imread("image.jpg")
image = cv2.resize(image, (506, 317))
height, width, _ = image.shape
center_coordinates = (width // 2, height // 2)
res = cv2.circle(image, center_coordinates, 120, (0, 255, 0), 10)
cv2.imshow('WINDOW', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/491abe87-e93f-4c85-bc41-31825e6d658b)

(3) Draw a rectangle around a specific region of interest in the image.

```
import cv2
image = cv2.imread("image.jpg")
image = cv2.resize(image, (506, 317))
start = (150, 100)
stop = (300, 200)
color = (255, 255, 100)
thickness = 10           
res_img = cv2.rectangle(image, start, stop, color, thickness)
cv2.imshow('WINDOW', res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/62bb5c4b-dada-478c-ba89-d293016c4e89)

(4) Add the text "OpenCV Drawing" at the top-left corner of the image.
```
import cv2
image = cv2.imread("forest.png")
image = cv2.resize(image, (400, 300))
text = "OpenCV Drawing"
position = (10, 50)
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255) 
thickness = 2
res = cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
cv2.imshow('WINDOW', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/d4f6c52c-277e-4c9b-8af1-6ea38dab2856)

### iii)Image Color Conversion
(1) Convert the image from RGB to HSV and display it
```
import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(300,200))
cv2.imshow('ORIGINAL IMAGE',image)
hsv = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/14d5c925-1cce-44ef-bf7a-4018adec47ee)

![image](https://github.com/user-attachments/assets/4ea03979-7d33-4fc7-af0c-ddf28c42a3fd)

(2) Convert the image from RGB to GRAY and display it.
```
import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(300,200))
cv2.imshow('ORIGINAL IMAGE',image)
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/e588c2a8-97ef-453e-a7da-1a41f8ed9b6a)

![image](https://github.com/user-attachments/assets/29c31910-78ea-405b-98f0-725081def0f2)

(3) Convert the image from RGB to YCrCb and display it.
```
import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(300,200))
cv2.imshow('ORIGINAL IMAGE',image)
YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/668cc166-9c52-42f8-82de-e90669f1198b)

![image](https://github.com/user-attachments/assets/51b87f81-2e23-4240-993d-546f33f02297)

(4) Convert the HSV image back to RGB and display it.
```
import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(300,200))
cv2.imshow('ORIGINAL IMAGE',image)
RGB = cv2.cvtColor(image,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/5d8d594f-00d0-4afd-9e0d-7a1319439d11)

![image](https://github.com/user-attachments/assets/6573e1aa-042e-4bb9-b7bb-b7fcde7703e1)

### iv)Access and Manipulate Image Pixels
(1) Access and print the value of the pixel at coordinates (100, 100)
```
pixel_value = image[100, 100]
print(f"Pixel value at (100, 100): {pixel_value}")
```
![image](https://github.com/user-attachments/assets/ede3f245-4cec-45fc-a538-53938a72619d)

(2) Modify the color of the pixel at (200, 200) to white
```
import cv2
image = cv2.imread('forest.png',1)
image = cv2.resize(image,(400,300))
cv2.imshow('ORIGINAL IMAGE',image)
image[200, 200] = [255, 255, 255] 
cv2.imshow('MODIFIED IMAGE', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/1aa4721e-cc93-4998-bfb6-c43a8c0c36df)

![image](https://github.com/user-attachments/assets/4c972cf1-735b-40a2-9717-8b2f87e88d58)

### v)Image Resizing
Resize the original image to half its size and display it.
```
cv2.imshow('ORIGINAL IMAGE',image)
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
cv2.imshow('RESIZED IMAGE', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/1f4b3905-6ab0-4479-87a6-d546700b6396)

![image](https://github.com/user-attachments/assets/cbe6758b-4aa6-4182-bcd6-6d05f03d6e69)

### vi)Image Cropping
```
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
```
![image](https://github.com/user-attachments/assets/2d552444-bdce-421c-87ae-c827efbba474)

### vii)Image Flipping
(1) Flip the original image horizontally and display it.
```
import cv2
image = cv2.imread("forest.png")
image = cv2.resize(image,(300,200))
res=cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('ORIGINAL IMAGE',image)
cv2.imshow('FLIPPED IMAGE', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/f0e91186-95ca-406b-b29b-7c87c405fbd2)

![image](https://github.com/user-attachments/assets/0cacfda8-51d3-4ecb-aa51-3277c476b08b)

(2) Flip the original image vertically and display it.
```
import cv2
image = cv2.imread("forest.png")
image = cv2.resize(image,(300,200))
res=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('ORIGINAL IMAGE',image)
cv2.imshow('FLIPPED IMAGE', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![image](https://github.com/user-attachments/assets/86cdfad3-4c07-45e5-8e44-a3587b5a3898)

![image](https://github.com/user-attachments/assets/a46dd84a-6d95-4ee8-8d08-b7910be908fd)

### viii)Write and Save the Modified Image
Save the final modified image to your local directory.
```
import cv2
img = cv2.imread("forest.png")
img = cv2.resize(img,(300,200))
cv2.imwrite('boat_pic.jpg',img)
```

![image](https://github.com/user-attachments/assets/daef0d78-010e-4e12-a115-952f211bbf3d)

## Result:
Thus the images are read, displayed, and written ,and color conversion was performed  successfully using the python program.







