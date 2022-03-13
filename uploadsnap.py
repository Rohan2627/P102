import cv2

import dropbox

# SenyLL2QVzoAAAAAAAAAAQxMnmuBbAcCAuyDkzv_6QOAvDchkTarMF59w_gIiZIP

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image = "NewPicture1.jpg"
        cv2.imwrite( image ,frame)
        result = False

    # releases the camera
    videoCaptureObject.release()

    return image
    
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()


def uploadFile():
    accessToken = "SenyLL2QVzoAAAAAAAAAAQxMnmuBbAcCAuyDkzv_6QOAvDchkTarMF59w_gIiZIP"

    image = take_snapshot()

    fileFrom = image
    fileTo = "/images/testFolder/" + (image)

    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom , 'rb') as f:
        dbx.files_upload(f.read() , fileTo , mode=dropbox.files.WriteMode.overwrite)

        print("Uploaded")


uploadFile()







