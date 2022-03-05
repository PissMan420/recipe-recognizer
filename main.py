import cv2

import recognizer


def on_key(key: int):
    if key == ord('q'):
        print('bye bye')
        cam.release()


cam = cv2.VideoCapture()
cam.open(0)
mat = None
color_conversion = None

while cam.isOpened():
    _succ, mat = cam.read()

    key = cv2.waitKey(10)
    if key == ord('q'):
        cam.release()
    elif key in [ord('c'), ord('z')]:
        if not color_conversion:
            color_conversion = 0
        if key == ord('c'):
            if color_conversion + 1 <= 143:
                if color_conversion + 1 == 8:
                    color_conversion += 2
                else:
                    color_conversion += 1
        elif key == ord('z'):
            if color_conversion - 1 > 0:
                color_conversion -= 1
        print('changing color conversion mode to %d' % color_conversion)
    if color_conversion:
        mat = cv2.cvtColor(mat, color_conversion)
    facture = recognizer.reconnaitre_facture(mat)
    cv2.imshow('recipe', facture)
