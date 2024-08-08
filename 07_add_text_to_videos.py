import cv2
import datetime
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#setting the frame height and width of the camera
#height, width property is having the property id instead of writing total property name
#whatever the maximum and minimum frame size you set, if it is beyond the
#camera limit then auto adjusted to the size of the camera

# cap.set(3, 3000)
# cap.set(4, 300)
#
# print(cap.get(3))
# print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Height :' + str(cap.get(4))
        datet = str(datetime.datetime.now())

        #in the place of text if you use datet, output will be the date and time
        cv2.putText(frame, text, (10, 50), font, 1,
                    (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()