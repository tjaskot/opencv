import cv2
import time
import PySimpleGUI as sg
from layout import layout as main2layout


sg.theme("LightGreen")

# Create the window and show it without the plot
window = sg.Window("OpenCV Integration", main2layout, location=(800, 400))

cap = cv2.VideoCapture('videos/dyna_pre.mp4')  # Has options, read, isOpened, release
# print(cap)  # prints memory object reference
# exit()

if not cap.isOpened():
    print("Video not located, please correct.")

# Instead of true, use isOpened for video, and potential repeat if needed
while cap.isOpened():
    res, frame = cap.read()
    print(res)

cap.release()
time.sleep(2)
window.close()




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
