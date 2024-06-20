from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd
import random as rd

# Set the background color and fonts
BACKGROUND_COLOR = "#B1DDC6"
FONT_L = ("Arial", 40, "normal")
FONT_T = ("Arial", 60, "bold")

# Load data
df = pd.read_csv("data/to_learn.csv")
to_learn = df.to_dict('records')

# Initial selection of a random dictionary
current = {}
q_word = ""
a_word = ""

# The next card
def next_card():
    global q_word, a_word, current
    if to_learn:
        current = rd.choice(to_learn)
        q_word = current["english"]
        a_word = current["amharic"]  # Correctly set to Amharic word
        canvas.itemconfig(card_text, text=q_word)
        canvas.itemconfig(card_title, text="English")
        canvas.itemconfig(image_background, image=front_img)
        window.after(3000, fliped_card)  # Flip the card after 3 seconds
    else:
        canvas.itemconfig(card_text, text="No more cards")
        canvas.itemconfig(card_title, text="")
        canvas.itemconfig(image_background, image=front_img)

# The current card answer
def fliped_card():
    canvas.itemconfig(card_text, text=a_word)
    canvas.itemconfig(card_title, text="Amharic")
    canvas.itemconfig(image_background, image=back_img)

def is_known():
    global to_learn
    if current in to_learn:
        to_learn.remove(current)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv")


# Create the main window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)

# Load images
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

# Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
image_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=FONT_L)
card_text = canvas.create_text(400, 263, text="", fill="black", font=FONT_T)

# Create buttons
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
# Start with the first card
next_card()

# Start the main loop
window.mainloop()
