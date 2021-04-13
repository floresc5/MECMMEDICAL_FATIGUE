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
#Convert 1 image from RGB to grayscale
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = mpimg.imread(r'C:\Users\flore\PycharmProjects\HandlingDatabases\save\videos\flores\0.png')
gray = rgb2gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()

##
#Save image as pixel array
img = cv2.imread(r'C:\Users\flore\PycharmProjects\HandlingDatabases\save\videos\flores\0.png')

