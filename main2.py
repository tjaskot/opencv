import os
import cv2
import copy
import json
import time
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
    layout_dict = dict

    def __init__(self):
        self.text = []  # Array for PySimpleGUI.Text()
        self.image = []  # Array for PySimpleGUI.Image()
        self.thres_slider = []  # Array, instead of list
        self.canny_slider = []  # Array, instead of list
        self.blur_slider = []  # Array, instead of list
        self.hue_slider = []  # Array, instead of list
        self.enhance_slider = []  # Array, instead of list
        self.exit_button = []  # Array, instead of list

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


# Instantiate class object for PySimpleGUI updates and reusable code
my_c = Layout()

# Create separate dictionary items and then have those accessible to add/update
layout_text = PySimpleGUI.Text("OpenCV Demo", size=(60, 1), justification="center")
# Need to use copy.copy for object addition to array as list exits if not list type
my_c.text.append(
    copy.copy(
        layout_text
    )
)
my_c.layout_dict.update(layout_text)
print(my_c.layout_dict)
exit()
my_c.image.append(
    copy.copy(
        PySimpleGUI.Image(filename="", key="-IMAGE-")
    )
)
my_c.thres_slider.append(
    # copy.copy(
        layout.add_slider(
            radio_name="threshold",
            radio_key="-THRESH-",
            slider_key="-THRESH SLIDER-"
        )
    # )
)
my_c.canny_slider.append(
    copy.copy(
        layout.add_slider(
            radio_name="canny",
            radio_key="-CANNY-",
            slider_key="-CANNY-",
            slider_size=(20, 15)
        )
    )
)
my_c.blur_slider.append(
    copy.copy(
        layout.add_slider(
            radio_name="blur",
            radio_key="-BLUR-",
            slider_key="-BLUR SLIDER-",
            slider_range=(1, 11),
            slider_default=1
        )
    )
)
my_c.hue_slider.append(
    copy.copy(
        layout.add_slider(
            radio_name="hue",
            radio_key="-HUE-",
            slider_default=0,
            slider_key="-HUE SLIDER-")
    )
)
my_c.enhance_slider.append(
    copy.copy(
        layout.add_slider(
            radio_name="enhance",
            radio_key="-ENHANCE-",
            slider_key="-ENHANCE SLIDER"
        )
    )
)
my_c.exit_button.append(
    copy.copy(
        PySimpleGUI.Button("Exit", size=(10, 1))
    )
)

for i in my_c:
    print(i)
exit()

window_layout = list
# TODO for i in my_c items, append to list, then you have layout
print(my_c.text)


exit()
with open("layout.json", "w") as layout_json, open("layout.py", "r") as layout_py:
    l_py_txt = layout_py.read().splitlines()
    json.dump(l_py_txt[2:], layout_json)

exit()

sg.theme("LightGreen")
# Create the window and show it without the plot
window = sg.Window("OpenCV Integration", window_layout, location=(800, 400))
cap = cv2.VideoCapture('videos/dyna_pre.mp4')  # Has options, read, isOpened, release
# print(cap)  # prints memory object reference
# Instead of true, use isOpened for video, and potential repeat if needed
if not cap.isOpened():
    print("Video not located, please correct.")
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
