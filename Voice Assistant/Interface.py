"""
Main interface
"""
from tkinter import *

from PIL import ImageTk, Image

import VoiceRecognition

# welcome audio to be played when gui launches
VoiceRecognition.welcome_note()


# function to terminate the interface
def terminate():
    root.destroy()


root = Tk()
root.iconbitmap("images/download.ico")
root.title("Voice Assistant")

root_window_width = 400
root_window_height = 400

# get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - root_window_width / 2)
center_y = int(screen_height / 2 - root_window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{root_window_width}x{root_window_height}+{center_x}+{center_y}')

heading = Label(root, text="_CYNTHIA_", font=("Helvetica", 18, "bold")).pack()
heading2 = Label(root, text="Your Personal Voice Assistant", font=("Arial", 10, "italic")).pack()

img = ImageTk.PhotoImage(Image.open("images/download.png"))
img_label = Label(root, image=img, height=150, width=150, borderwidth=5).pack(pady=20)


# function for the button
def convert():
    try:
        converted_text = VoiceRecognition.speech_to_text()
        returnMsg = VoiceRecognition.process_command(converted_text)

        converted_text_label.config(text=converted_text)

        if (returnMsg == "stop"):
            root.destroy()

    except Exception as e:
        print(e)


mic_image = ImageTk.PhotoImage(Image.open("images/mic.png").resize((80, 80)))

mic_button = Button(root, image=mic_image, borderwidth=5, padx=5, pady=5, height=40, width=40, command=convert)
mic_button.pack(pady=10)

converted_text_label = Label(root)
converted_text_label.pack(pady=5)

root.mainloop()
