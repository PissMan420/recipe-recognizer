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
    facture = recognizer.reconnaitre_facture(mat)
    cv2.imshow('recipe', facture)
