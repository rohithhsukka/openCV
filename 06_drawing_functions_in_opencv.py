#importing numpy(numerical python) and cv2(Computer vision) libraries
import numpy as np
import cv2

#creating a imag variable by taking input as jpg image
#img = cv2.imread('02_lena.jpg',1)

#creating a black image with numpy using zeroes method
img = np.zeros([512, 512, 3], np.uint8)

#drawing a line on image
img = cv2.line(img, (0,0), (255,255), (155,235,52), 10)  #52, 235, 155

# drawing a arrowed line in an image
img = cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)

#drawing a rectangle in an image
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 10)

#drawing a circle filled with color in an image
img = cv2.circle(img, (447, 63), 63, (0,255,0), -1)

#writing a text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10,500), font, 4, (0,255,255), 10, cv2.LINE_AA)

#to show image
cv2.imshow('image',img)

#to avoid closing the winow opened instantly
cv2.waitKey(0)

#closing all the opened windows
cv2.destroyAllWindows()