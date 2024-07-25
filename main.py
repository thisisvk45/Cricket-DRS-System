
# Required Modules
import tkinter as tk  # For creating GUI
import cv2  # OpenCV (pip install opencv-python)
from PIL import Image, ImageTk  # Python Imaging Library (pip install pillow)
from functools import partial  # For passing arguments into functions
import threading  # Prevents program blocking
import imutils  # Resizes photos
import time  # For time delays

# Global Variables
SET_WIDTH = 650
SET_HEIGHT = 368
flag = True
stream = cv2.VideoCapture("clip5.mp4")

# Function to control video playback speed
def play(speed):
    global flag
    frame_pos = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame_pos + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        return

    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)

    if flag:
        canvas.create_text(170, 25, fill="red", font="Times 27 italic bold", text="Decision Pending...")
    flag = not flag

    print(f"You clicked on play. Speed is {speed}")

# Function to handle the decision process
def pending(decision):
    show_image("pending.png", 2)
    show_image("sponsor.png", 1.5)
    show_image(f"{decision}.png")

def show_image(image_path, delay=0):
    frame = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)
    if delay > 0:
        time.sleep(delay)

# Function to handle out decision
def out():
    threading.Thread(target=pending, args=("out",), daemon=True).start()
    print("Player is out")

# Function to handle not out decision
def not_out():
    threading.Thread(target=pending, args=("not out",), daemon=True).start()
    print("Player is not out")

# GUI Setup
window = tk.Tk()
window.title("Vikas's Third Umpire Decision Review System")

# Display the welcome image
canvas = tk.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
welcome_img = cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
welcome_img = ImageTk.PhotoImage(image=Image.fromarray(welcome_img))
canvas.create_image(0, 0, anchor=tk.NW, image=welcome_img)
canvas.pack()

# Buttons to control playback
btn_texts = [("<< Previous (Fast)", -25), ("<< Previous (Slow)", -2), ("Previous (Slower)", -1), 
             ("Next (Fast) >>", 25), ("Next (Slow) >>", 2), ("Next (Slower) >>", 1)]
for text, speed in btn_texts:
    tk.Button(window, text=text, width=50, command=partial(play, speed)).pack()

# Buttons to give decisions
tk.Button(window, text="Give Out!", width=50, command=out).pack()
tk.Button(window, text="Give Not Out!", width=50, command=not_out).pack()

window.mainloop()
"""
Name: Third Umpire Decision Review System
Author: Vikas Kumar
"""
