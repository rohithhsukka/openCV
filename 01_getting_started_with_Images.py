#importing openCV library
import cv2

#reading image
img = cv2.imread('02_lena.jpg', -1)

#printing the image values stored in the format of numpy array
print(img)

#showing the image in window
cv2.imshow('image', img)

#To Not close the window instantly
k = cv2.waitKey(0)

#Conditon for checking does the escape button is pressed
if k == 27:
    cv2.destroyAllWindows()

#if 'S' is pressed in keyboard then save the copy of image
elif k == ord('s'):
    #creating the image
    cv2.imwrite('03_lena_copy.png', img)
    #closing all the opened windows
    cv2.destroyAllWindows()