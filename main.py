# https://realpython.com/pysimplegui-python/   - guided reference

import os
import cv2
import time
import PySimpleGUI as sg
from layout import manual_layout


layout = manual_layout

# for i in layout:
#     for j in i:
#         print(type(j))
# exit()

sg.theme("LightGreen")
# Create the window and show it without the plot
#    print(sg.Window.get_screen_size())
#    w, h = sg.Window.get_screen_size()
#    print ('w: ', w)
#    print ('h: ', h)
window = sg.Window("OpenCV Integration", layout, location=(0, 0), grab_anywhere=True).Finalize()

# If window needs to be full screen, uncomment line below
# window.Maximize()

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('videos/dyna_pre.mp4')

while True:
    event, values = window.read(timeout=20)
    print(event)
    print(values)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    ret, frame = cap.read()

    if values["-THRESH-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)[:, :, 0]
        frame = cv2.threshold(
            frame, values["-THRESH SLIDER-"], 255, cv2.THRESH_BINARY
        )[1]
    elif values["-CANNY-"]:
        frame = cv2.Canny(
            frame, values["-CANNY SLIDER A-"], values["-CANNY SLIDER B-"]
        )
    elif values["-BLUR-"]:
        frame = cv2.GaussianBlur(frame, (21, 21), values["-BLUR SLIDER-"])
    elif values["-HUE-"]:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] += int(values["-HUE SLIDER-"])
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    elif values["-ENHANCE-"]:
        enh_val = values["-ENHANCE SLIDER-"] / 40
        clahe = cv2.createCLAHE(clipLimit=enh_val, tileGridSize=(8, 8))
        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        lab[:, :, 0] = clahe.apply(lab[:, :, 0])
        frame = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    else:
        pass

    # calculate the 50 percent of original dimensions
    width = int(frame.shape[1] * 50 / 100)
    height = int(frame.shape[0] * 50 / 100)
    dsize = (width, height)

    # resize image for display only - save the full resolution for the write to file
    display = cv2.resize(frame, dsize)
    imgbytes = cv2.imencode(".png", display)[1].tobytes()
    window["-IMAGE-"].update(data=imgbytes)

window.close()
