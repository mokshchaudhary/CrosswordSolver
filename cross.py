# Author: Moksh Chaudhary
# Github: www.github.com/mokshchaudhary

import mss #faster Screenshot than pyautogui
import cv2
import numpy as np
import pyautogui as p
import os

monitor = {"top":270,"left":20,"width":20,"height":20} #Defines the area of a single 'box' of crossword
f="ETAONIHSRLDUCMWYFGPBVKJXQZ" #Based on frequency of alphabets in English Language
p.PAUSE=0 #Defines the pause between clicks

# Processes Image
def impro(img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Turns it into Grayscale
        ret, thresh = cv2.threshold(img,180,255,cv2.THRESH_BINARY_INV) #Threhold Read more at: https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
        img = cv2.bitwise_not(thresh) # Bitwise Not
        return img # returns the processed image

for i in range(26):
        x=y=0
        for x in range(13):
                os.system('clear') #Change to cls if you're on windows
                print("Testing: ",f[i]) #Print the Alphabet being Tested
                for y in range(13):
                        with mss.mss() as sct:
                                img=sct.grab(monitor) #Takes the screenshot
                        img=np.array(img) #Converts the capture to numpy array                    
                        img=impro(img)
                        
                        if not np.mean(img)<240: #Threshold of the white in the box, Checks if the box is empty
                                p.click(monitor["left"],monitor["top"],clicks=2) #Clicks on the box currently being checked
                                p.press(f[i],interval=0.017) #Clicks the alphabet
                                p.click(81,910,clicks=2) #Clicks "Check All" button
                        monitor["left"]=monitor["left"]+40 #Moves to next box
                monitor["top"]=monitor["top"]+40 #Moves to next line
                monitor["left"]=20 #Sets the left cordinate to starting again
                y=0
        monitor = {"top":270,"left":20,"width":20,"height":20} #Sets it back to starting position
print("Solved :)") # Hopefully