import cv2


def take_snapshot():
    #initializing cv2
    #this will start the webcam
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
        #read the frames while the camera is on
        #ret is a dummy variable which returns a boolean value 
        #basically to tell us if something is being returned or not
        #frame is a variable that has a frame of the video
        ret,frame = videoCaptureObject.read()
        print("frame ", frame)

        #cv2.imwrite("filename",image) method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)

        result = False

    #release the camera - to close the webcam
    videoCaptureObject.release()

    #close all the open windows that might be opened by the camera whie this process
    cv2.destroyAllWindows()

take_snapshot()