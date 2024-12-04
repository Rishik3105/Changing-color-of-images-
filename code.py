import cv2 as cv
print("1.colour to black and white \n 2. Black and white to Colour")
choice=int(input("enter your choice"))
img_path=input("Give your image path")
img=cv.imread(img_path)
if choice==1:
    gray_image=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray_image",gray_image)
if choice==2:
    color_image=cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    cv.imshow("Colour_image",color_image)
cv.waitKey(0)
