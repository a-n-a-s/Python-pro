import cv2
img_location = "C:\\Users\\ADmin\\Downloads\\download.jpg"
img = cv2.imread(img_location)

gray_image = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
inveretd_grey_image = 255 - gray_image
blur_img = cv2.GaussianBlur(inveretd_grey_image,(21,21) , 0)
inverted_blur_img = 255 - blur_img
pencil_sketch = cv2.divide(gray_image , inverted_blur_img ,scale=256.0)
 
cv2.imshow('Original Image' , img)
cv2.imshow('New Image ' , pencil_sketch)
cv2.waitKey(0)