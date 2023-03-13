import PySimpleGUI
import copy


def add_slider(radio_name, radio_key, slider_key, radio_type="Radio", radio_size=(10, 1), slider_default=128,
               slider_size=(40, 15), slider_range=(0, 255), slider_tick=1, slider_orientation="h"):
    """
    Function call to add Radio button and Slider component to layout.

    Args:
        radio_name: Name of Radio PySimpleGUI, needs to be defined
        radio_key: Key of Radio PySimpleGui, needs to be defined
        slider_key: Key of Slider, needs to be defined
        radio_type: Radio type can be defined, default "Radio"
        radio_size: Radio size is changeable, default (10,1)
        slider_default: Default Slider position of 128
        slider_size: Default slider size of (40, 15)
        slider_range: Default slider range of 0 to 255, written as (0, 255)
        slider_tick: Default slider movements, default is 1
        slider_orientation: Default slider orientation is horizontal, written as "h"

    Default Slider configs:
    PySimpleGUI.Slider(
        (0, 255),
        128,
        1,
        orientation="h",
        size=(40, 15),
        key=<Slider Key>,
    )

    Returns: slider_list with radio button and slider objects

    """
    slider_list = []  # Array needed for objects added to list
    # Example: sg.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-")
    # print(radio_key)
    layout_radio = PySimpleGUI.Radio(radio_name, radio_type, radio_size, radio_key)
    # print(layout_radio.Key)
    slider_list.append(layout_radio)
    # We need to verify with Radio key if the slider will be Canny, then add two slider key objects instead of one
    if radio_key == "-CANNY-":
        for canny_slider_key in ["-CANNY SLIDER A-", "-CANNY SLIDER B-"]:
            layout_slider_canny = PySimpleGUI.Slider(
                slider_range,
                slider_default,
                slider_tick,
                orientation=slider_orientation,
                size=slider_size,
                key=canny_slider_key
            )
            slider_list.append(layout_slider_canny)
    else:
        layout_slider = PySimpleGUI.Slider(
            slider_range,
            slider_default,
            slider_tick,
            orientation=slider_orientation,
            size=slider_size,
            key=slider_key
        )
        slider_list.append(layout_slider)
    return slider_list


# def set_gui_text(title=None, sizing=None, justifys=None):
#     # Example: sg_obj.Text("OpenCV Demo", size=(60, 1), justification="center")
#     sg_obj = PySimpleGUI.Text()
#     if title is None:
#         title = "OpenCV Demo"
#     if sizing is None:
#         sizing = (60, 1)
#     if justifys is None:
#         justifys = "center"
#     sg_obj.Text(title, size=sizing, justification=justifys)
#     return sg_obj.Text

# JSON object for manipulation when needed where Class objects don't suffice.
#  - Can repurpose dict values to PySimpleGUI objects.
#  - Example:   layout_json["sg_image"]= [], layout_json["sg_image"] = PySimpleGUI.Image(<parameters>)
layout_json = {
    "sg_text": [
        "sg_text"
    ],
    "sg_image": [
        "sg_image"
    ],
    #        [sg.Radio("None", "Radio", True, size=(10, 1))],
    "sg_thres": [],
    "sg_canny": [],
    "sg_blur": '"sg_radio", "sg_slider"',
    "sg_hue": '"sg_radio", "sg_slider"',
    "sg_enhance": '"sg_radio", "sg_slider"',
    "sg_button": [
        "sg_button"
    ]
}

manual_layout = [
    [PySimpleGUI.Text("OpenCV Demo", size=(60, 1), justification="center")],
    [PySimpleGUI.Image(filename="", key="-IMAGE-")],
    #        [PySimpleGUI.Radio("None", "Radio", True, size=(10, 1))],
    [
        PySimpleGUI.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"),
        PySimpleGUI.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(40, 15),
            key="-THRESH SLIDER-",
        ),
    ],
    [
        PySimpleGUI.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
        PySimpleGUI.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(20, 15),
            key="-CANNY SLIDER A-",
        ),
        PySimpleGUI.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(20, 15),
            key="-CANNY SLIDER B-",
        ),
    ],
    [
        PySimpleGUI.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
        PySimpleGUI.Slider(
            (1, 11),
            1,
            1,
            orientation="h",
            size=(40, 15),
            key="-BLUR SLIDER-",
        ),
    ],
    [
        PySimpleGUI.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
        PySimpleGUI.Slider(
            (0, 225),
            0,
            1,
            orientation="h",
            size=(40, 15),
            key="-HUE SLIDER-",
        ),
    ],
    [
        PySimpleGUI.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
        PySimpleGUI.Slider(
            (1, 255),
            128,
            1,
            orientation="h",
            size=(40, 15),
            key="-ENHANCE SLIDER-",
        ),
    ],
    [PySimpleGUI.Button("Exit", size=(10, 1))],
]
