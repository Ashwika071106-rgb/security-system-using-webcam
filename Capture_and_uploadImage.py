import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)

    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while(result):
        ret,frame = videoCaptureObject.read()

        img_name = "img" + str(number) + ".png"

        cv2.imwrite(img_name,frame)

        start_time = time.time
        result = False
    print("Snapshot taken")

    videoCaptureObject.release()

    cv2.destroyAllWindows()

    return img_name
    

def upload_file(img_name):
    access_token = '85wzTjuDVBwAAAAAAAAAAQmWmhyGrn6ovC77rlJXVOVfwU4Kuij-vP132Pnzmmz-'
    file = img_name
    file_from = file
    file_to  = "/NewFolder1/" + (img_name) 
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f :
        #mode = dropbox.files.WriteMode.overwrite is used to resolve path errors
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time() - start_time ) >= 300):
            print("snap")
            name = take_snapshot()
            upload_file(name)
main()