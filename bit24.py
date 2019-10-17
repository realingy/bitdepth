import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import cv2 as cv

# path = '../data/src/'
path = './data/'
images = os.listdir(path)

def process_image(img):
    return img

if __name__ == '__main__':
    for i in images:
        img_path = os.path.join(path , i)
        img_path = os.path.join('./data/', i)
        img = cv.imread(img_path)
        img = process_image(img)
        save_path = os.path.join('./data/', i)
        print("processing", i)
        cv.imwrite(img_path, img)



