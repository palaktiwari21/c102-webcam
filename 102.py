import dropbox
import cv2
import time
import random

start_time=time.time() #this will return time in floating point numbers
def take_snapshot():
    number=random.randint(0,100) #this will generate random integer
    videoCaptureObject=cv2.VideoCapture(0) #initialisng the library,this will start the web cam
    result=True
    while(result):
        ret,frame=videoCaptureObject.read() #ret is dumy variable , read is used to read frames , frame will have the pictures
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame) #imwrite function is used to save the image.
        result=False
        return(img_name)
    print('snapshot taken')
    videoCaptureObject.release() #release method is used to close the web cam
    cv2.destroyAllWindows() #this methood is to close any window opened by camera
#take_snapshot()

def upload_image(img_name):
    access_token='alKsCBAZHewAAAAAAAAAAX8w14PY7_xhMnDqNqXpaJFdg1JFlVK7-UV_w3_lAPVV'
    file=img_name
    file_from=file
    file_to='/snapshots/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        print(time.time()-start_time)
        if ((time.time()-start_time)>=15):
            name=take_snapshot()
            upload_image(name)
main()