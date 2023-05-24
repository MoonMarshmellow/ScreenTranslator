import time
import cv2
import pytesseract
import numpy
from PIL import ImageGrab
import pyautogui
from translate import Translator

prevtext = '0'

print('Please place mouse over the first corner of the scanning area:')
print('Scanning in 2 seconds')
time.sleep(2)
x1 = pyautogui.position().x
y1 = pyautogui.position().y
print(pyautogui.position())
print('Scanning in 3 seconds')
time.sleep(3)
x2 = pyautogui.position().x
y2 = pyautogui.position().y
print(pyautogui.position())


def transtode(text):
    translator = Translator(from_lang='de',to_lang='en')
    print(translator.translate(str(text)))




while True:
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    imgarr = numpy.array(img)
    cv2.imshow('cum', imgarr)

    rawtext = pytesseract.image_to_string(imgarr)
    text = str(rawtext)



    if prevtext != text and isinstance(text, str):
        #print(text)
        transtode(text)
  

    prevtext = text
    
             

    if cv2.waitKey(1) == 27:
        break