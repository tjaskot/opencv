import os
import cv2
import copy
import json
import time
import layout
import PySimpleGUI
import PySimpleGUI as sg


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
        return (f"Layout Inner Class Properties:\n"
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
layout_list = list()

# Create separate dictionary items and then have those accessible to add/update
layout_text = PySimpleGUI.Text("OpenCV Demo", size=(60, 1), justification="center")
# Need to use copy.copy for object addition to array as list exits if not list type
#   - Note: can use array type without copy or deepcopy, but could cause memory reference issue
my_c.text.append(
    copy.copy(
        layout_text
    )
)
layout_list.append([layout_text])

layout_image = PySimpleGUI.Image(filename="", key="-IMAGE-")
my_c.image.append(
    copy.copy(
        [layout_image]
    )
)
layout_list.append([layout_image])

layout_thres_slider = layout.add_slider(
    radio_name="threshold",
    radio_key="-THRESH-",
    slider_key="-THRESH SLIDER-"
)
my_c.thres_slider.append(
    copy.copy(
        layout_thres_slider
    )
)
layout_list.append(layout_thres_slider)

layout_canny_slider = layout.add_slider(
    radio_name="canny",
    radio_key="-CANNY-",
    slider_key="-CANNY-",
    slider_size=(20, 15)
)
my_c.canny_slider.append(
    copy.copy(
        layout_canny_slider
    )
)
layout_list.append(layout_canny_slider)

layout_blur_slider = layout.add_slider(
    radio_name="blur",
    radio_key="-BLUR-",
    slider_key="-BLUR SLIDER-",
    slider_range=(1, 11),
    slider_default=1
)
my_c.blur_slider.append(
    copy.copy(
        layout_blur_slider
    )
)
layout_list.append(layout_blur_slider)

layout_hue_slider = layout.add_slider(
    radio_name="hue",
    radio_key="-HUE-",
    slider_default=0,
    slider_key="-HUE SLIDER-"
)
my_c.hue_slider.append(
    copy.copy(
        layout_hue_slider
    )
)
layout_list.append(layout_hue_slider)

layout_enhance_slider = layout.add_slider(
    radio_name="enhance",
    radio_key="-ENHANCE-",
    slider_key="-ENHANCE SLIDER"
)
my_c.enhance_slider.append(
    copy.copy(
        layout_enhance_slider
    )
)
layout_list.append(layout_enhance_slider)

layout_button = PySimpleGUI.Button("Exit", size=(10, 1))
my_c.exit_button.append(
    copy.copy(
        layout_button
    )
)
layout_list.append([layout_button])

print(layout_list)
# Return repr for class object so we can verify all PySimpleGUI objects were created.
# print(my_c)
# Show all attributes of created object, and if introspection attributes does not have __ prefix or __ suffix, then is
#   attribute of class object instantiated
# print(dir(my_c))
# exit()

local_json = layout.layout_json
local_json["sg_text"] = my_c.text
local_json["sg_image"] = my_c.image
local_json["sg_thres"] = my_c.thres_slider
local_json["sg_canny"] = my_c.canny_slider
local_json["sg_blur"] = my_c.blur_slider
local_json["sg_hue"] = my_c.hue_slider
local_json["sg_enhance"] = my_c.enhance_slider
local_json["sg_button"] = my_c.exit_button

# for layout_item_name, layout_item_value in local_json.items():
#     print(layout_item_name)
#     print(layout_item_value)
# exit()

PySimpleGUI.theme("LightGreen")
# print(layout.manual_layout)
# print(dir(layout.manual_layout[0][0]))
# print(layout.manual_layout[2][0].Key)
# print(layout_list[2][0].Key)
# exit()
# Create the window and show it without the plot
window = PySimpleGUI.Window("OpenCV Integration", layout.manual_layout, location=(800, 400))
# window = PySimpleGUI.Window("OpenCV Integration", layout_list, location=(800, 400))
cap = cv2.VideoCapture('videos/dyna_pre.mp4')  # Has options, read, isOpened, release
# cap = cv2.VideoCapture(0)  # Get user video
# print(cap)  # prints memory object reference
# Instead of true, use isOpened for video, and potential repeat if needed
if not cap.isOpened():
    print("Video not located, please correct.")
# TODO: open one frame, then with button continue to video
# exit()

while True:
    event, values = window.read(timeout=20)
    # print(values)
    if event == "Exit" or event == PySimpleGUI.WIN_CLOSED:
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

# TODO: next is to create Def that extracts all introspected attributes without a __ prefix or __ suffix
