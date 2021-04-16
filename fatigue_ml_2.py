import cv2
import os
from glob import glob
##
#extract frames from video at a specific rate
#frame rate specified: every 10 frames
def create_dir(path): #finding name of file to create path
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap = 10): #saving every 10th frame of selected video path
    name = video_path.split("/")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    create_dir(save_path)

    cap = cv2.VideoCapture(video_path)
    idx = 0

    while True: #index each frame by number

        ret, frame = cap.read()


        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}/{idx}.png", frame)


        idx += 1

if __name__ == "__main__": #save indexed frame in folder
    video_paths = glob("videos/*")
    save_dir = "save"

for path in video_paths:
    save_frame(path, save_dir, gap=10)
    ##
    #This is the face recognition script. We do not know how to incorporate it into the previous loop to save
    #the cropped ROI
import cv2
imagePath = r"C:\Users\flore\PycharmProjects\HandlingDatabases\save\videos\Lopez\0.png"
cascPath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
img = cv2.imread(imagePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

for (x, y, w, h) in faces:
    roi = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    crop_img = img[y:y + h, x:x + w]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
