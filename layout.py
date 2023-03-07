import PySimpleGUI as sg

layout = [
    [sg.Text("OpenCV Demo", size=(60, 1), justification="center")],
    [sg.Image(filename="", key="-IMAGE-")],
    #        [sg.Radio("None", "Radio", True, size=(10, 1))],
    [
        sg.Radio("threshold", "Radio", size=(10, 1), key="-THRESH-"),
        sg.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(40, 15),
            key="-THRESH SLIDER-",
        ),
    ],
    [
        sg.Radio("canny", "Radio", size=(10, 1), key="-CANNY-"),
        sg.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(20, 15),
            key="-CANNY SLIDER A-",
        ),
        sg.Slider(
            (0, 255),
            128,
            1,
            orientation="h",
            size=(20, 15),
            key="-CANNY SLIDER B-",
        ),
    ],
    [
        sg.Radio("blur", "Radio", size=(10, 1), key="-BLUR-"),
        sg.Slider(
            (1, 11),
            1,
            1,
            orientation="h",
            size=(40, 15),
            key="-BLUR SLIDER-",
        ),
    ],
    [
        sg.Radio("hue", "Radio", size=(10, 1), key="-HUE-"),
        sg.Slider(
            (0, 225),
            0,
            1,
            orientation="h",
            size=(40, 15),
            key="-HUE SLIDER-",
        ),
    ],
    [
        sg.Radio("enhance", "Radio", size=(10, 1), key="-ENHANCE-"),
        sg.Slider(
            (1, 255),
            128,
            1,
            orientation="h",
            size=(40, 15),
            key="-ENHANCE SLIDER-",
        ),
    ],
    [sg.Button("Exit", size=(10, 1))],
]
