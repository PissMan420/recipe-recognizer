#/bin/python3
import sys

import cv2
import glfw
import imgui
import OpenGL.GL as gl

from imgui.integrations.glfw import GlfwRenderer

import recognizer


def on_key(key: int):
    if key == ord('q'):
        print('bye bye')
        cam.release()


cam = cv2.VideoCapture()
cam.open(0)
mat = None
color_conversion = None
imgui.create_context()
glfw.init()
WIN_TITLE = 'recipe recognition'
if sys.platform == 'darwin':
    # Mac OS Specific hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.COCOA_RETINA_FRAMEBUFFER, True)
    glfw.window_hint(glfw.COCOA_GRAPHICS_SWITCHING, gl.GL_TRUE)
    glfw.window_hint_string(glfw.COCOA_FRAME_NAME, WIN_TITLE)
elif sys.plarform in ['linux', 'linux2']:
    # Linux Specific hints
    glfw.window_hint_string(glfw.X11_CLASS_NAME, 'cls' + WIN_TITLE)
    glfw.window_hint_string(glfw.X11_INSTANCE_NAME, WIN_TITLE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)
window = glfw.create_window(1280, 720, WIN_TITLE, None, None)
glfw.make_context_current(window)
if not window: exit(1)

while cam.isOpened():
    _succ, mat = cam.read()

    facture = recognizer.reconnaitre_facture(mat)
    cv2.imshow('recipe', facture)
