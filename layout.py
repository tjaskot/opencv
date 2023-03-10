import PySimpleGUI


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
    layout_radio = PySimpleGUI.Radio(radio_name, radio_type, radio_size, radio_key)
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
