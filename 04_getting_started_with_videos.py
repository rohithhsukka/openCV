#importing the OpenCV library
import cv2

#video capturinng through different cams and also the video file can be inserted
cap = cv2.VideoCapture(0)

#four character code used for different media(video) formats
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#creating a video capured from the cam and saving it
out = cv2.VideoWriter('05_output.avi', fourcc, 20.0, (640,480))

#to check video capturing is already enabled
print(cap.isOpened())


while(cap.isOpened()):
    #storing the video in frame variable and ret is boolean value which tells is the video is captured
    ret, frame = cap.read()

    if ret == True:

        #to get the frame width
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #to get the frame height
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        #writing the video file
        out.write(frame)

        #converting color image to grey color image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #showing image in window
        cv2.imshow('frame', gray)

        #condtion to quit the window
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

#Closes video file or capturing device
cap.release()
out.release()

#closing all the opened windows
cv2.destroyAllWindows()