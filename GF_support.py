from tkinter import *
import random
import urllib.request
from PIL import Image, ImageTk
import io

# Define mood ranges and corresponding messages
mood_ranges = [(1, 3), (3, 7), (7, 11)]
mood_messages = [
    "You're amazing and G loves you xxxx",
    "You're super amazing and G loves you xxxx",
    "You're super super amazing and G loves you xxxx"
]

# Define function to get a random image URL from the web
def get_random_image():
    response = urllib.request.urlopen('https://source.unsplash.com/1600x900/?love+impressionism')
    image_data = response.read()
    image = Image.open(io.BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    return photo

# Define function to update the mood message label based on the user's mood selection
def print_mood():
    try:
        mood = int(mood_var.get())
        for i, (low, high) in enumerate(mood_ranges):
            if low <= mood < high:
                mood_message.set(mood_messages[i])
                break
        love_image = get_random_image()
        love_label.config(image=love_image)
        love_label.image = love_image
        message_popup()
    except ValueError:
        mood_message.set("Please enter a smoochy number between 1 and 10.")

# Define function to create popup for mood message
def message_popup():
    popup = Toplevel(root)
    popup.title("Mood Message")
    popup.geometry("400x100")
    message_label = Label(popup, textvariable=mood_message)
    message_label.pack()
    ok_button = Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()

# Define main window
root = Tk()
root.title("GF Mood Emergency Support")
root.geometry("1200x800")

# Define label for mood selection
mood_label = Label(root, text="How do you feel from 1 to 10 my love?")
mood_label.pack()

# Define mood selection scale
mood_var = StringVar()
mood_scale = Scale(root, from_=1, to=10, orient=HORIZONTAL, variable=mood_var)
mood_scale.pack()

# Define button to submit mood selection
submit_button = Button(root, text="Click for some love", command=print_mood)
submit_button.pack()

# Define label for love image
love_image = get_random_image()
love_label = Label(root, image=love_image)
love_label.pack()

# Initialize mood message variable
mood_message = StringVar()
mood_message.set("")

# Start main loop
root.mainloop()
