import mss
import cv2
import numpy as np
import pyautogui as p
import os

monitor = {"top":270,"left":20,"width":20,"height":20}
f="ETAONIHSRLDUCMWYFGPBVKJXQZ"
p.PAUSE=0

def impro(img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV)
        img = cv2.bitwise_not(thresh)
        return img


i=0
while(i<26):
        x=y=0
        while(x<13):
                os.system('clear')
                print("Testing: ",f[i])
                while(y<13):
                        with mss.mss() as sct:
                                img=sct.grab(monitor)
                        img=np.array(img)
                        img=impro(img)
                        
                        if not np.mean(img)<240:
                                p.click(monitor["left"],monitor["top"],clicks=2)
                                p.press(f[i],interval=0.017)
                                p.click(81,910,clicks=2)
                        monitor["left"]=monitor["left"]+40
                        y=y+1
                monitor["top"]=monitor["top"]+40
                monitor["left"]=20
                x=x+1
                y=0
        monitor = {"top":270,"left":20,"width":20,"height":20}
        i=i+1
os.system('cowsay Solved This Bitch')