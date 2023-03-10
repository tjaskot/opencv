import os
import cv2
import time
import json
import layout
import PySimpleGUI

# class MyClass:
#     def __init__(self):
#         self.l = list
#
#     def __repr__(self):
#         return f'{self.l}'
#
#
# my_c = MyClass()
# my_c.l = ['1', '2']
# print(my_c.l)
# print(my_c)

# exit()

class Layout:
    def __init__(self):
        self.text = PySimpleGUI.Text()
        self.image = PySimpleGUI.Image()
        self.thres_slider = list
        self.canny_slider = list
        self.blur_slider = list
        self.hue_slider = list
        self.enhance_slider = list

    def __repr__(self):
        return (f"Layout Inner Class Properties -\n"
                f"Text object: {self.text}\n"
                f"Image object: {self.image}\n"
                f"Threshold object list: {self.thres_slider}\n"
                f"Canny object list: {self.canny_slider}\n"
                f"Blur object list: {self.blur_slider}\n"
                f"Hue object list: {self.hue_slider}\n"
                f"Enhance object list: {self.enhance_slider}\n"
                )


my_c = Layout()
my_c.text.DisplayText = "OpenCV Demo"
my_c.text.Size = (60, 1)
my_c.text.Justification = "center"
print(my_c.text)


exit()
with open("layout.json", "w") as layout_json, open("layout.py", "r") as layout_py:
    l_py_txt = layout_py.read().splitlines()
    json.dump(l_py_txt[2:], layout_json)

exit()

sg.theme("LightGreen")

# Create the window and show it without the plot
window = sg.Window("OpenCV Integration", main2layout, location=(800, 400))

cap = cv2.VideoCapture('videos/dyna_pre.mp4')  # Has options, read, isOpened, release
# print(cap)  # prints memory object reference
# exit()

if not cap.isOpened():
    print("Video not located, please correct.")

# Instead of true, use isOpened for video, and potential repeat if needed

# TODO: open one frame, then with button continue to video


exit()

while True:
    event, values = window.read(timeout=20)
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

    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["-IMAGE-"].update(data=imgbytes)

    window.close()

cap.release()
