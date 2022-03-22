#!/bin/python3
import sys
import random

import cv2
import glfw
import imgui
import OpenGL.GL as gl

from imgui.integrations.glfw import GlfwRenderer

import recognizer


def gl_load_texture(mat) -> int:
    """Load opencv `mat` into open gl. Return open gl texture id"""
    id = random.randint(1, 2**32)
    if len(mat) > 2:
        target = gl.GL_TEXTURE_2D
    else:
        target = gl.GL_TEXTURE_1D
    gl.glBindTexture(texture=id, target=target)
    gl.glTexImage2D(target, gl.GL_TEXTURE_RECTANGLE, gl.GL_RGB, len(mat[0]),
                    len(mat[1]), gl.GL_UNSIGNED_BYTE, mat)
    gl.glTexParameteri(target, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(target, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(target, gl.GL_TEXTURE_WRAP_S, gl.GL_CLAMP_TO_EDGE)
    gl.glTexParameteri(target, gl.GL_TEXTURE_WRAP_T, gl.GL_CLAMP_TO_EDGE)
    return id


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
if sys.platform == 'darwin': # Mac OS Specific hints
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.COCOA_RETINA_FRAMEBUFFER, True)
    glfw.window_hint(glfw.COCOA_GRAPHICS_SWITCHING, gl.GL_TRUE)
    glfw.window_hint_string(glfw.COCOA_FRAME_NAME, WIN_TITLE)
elif sys.plarform in ['linux', 'linux2']: # Linux Specific hints
    glfw.window_hint_string(glfw.X11_CLASS_NAME, 'cls' + WIN_TITLE)
    glfw.window_hint_string(glfw.X11_INSTANCE_NAME, WIN_TITLE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)
window = glfw.create_window(1280, 720, WIN_TITLE, None, None)
glfw.make_context_current(window)

while cam.isOpened():
    imgui.new_frame()

    imgui.end_frame()
    _succ, mat = cam.read()

    facture = recognizer.reconnaitre_facture(mat)
    cv2.imshow('recipe', facture)
