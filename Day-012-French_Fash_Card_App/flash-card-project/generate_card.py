from tkinter import Canvas, PhotoImage, Label, Button
import tkinter as tk
import pandas
import random

bg_color = "#B1DDC6"

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    word_list_dict = df.to_dict(orient="records")


class GenerateInterface(Canvas):
    def __init__(self):
        super().__init__()
        self.config(width=800, height=526, bg=bg_color, highlightthickness=0)

        self.card_front_img = PhotoImage(file="./images/card_front.png")
        self.card_back_img = PhotoImage(file="./images/card_back.png")
        self.right_img = PhotoImage(file="./images/right.png")
        self.wrong_img = PhotoImage(file="./images/wrong.png")

        self.card_bg = self.create_image(400, 263, image=self.card_front_img)
        self.language_text = self.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.word_text = self.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.word_known)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.word_not_known)
        self.right_button.grid(row=1, column=0)
        self.wrong_button.grid(row=1, column=1)

        self.grid(row=0, column=0, columnspan=2)

        self.flip_timer = None
        self.change_french()

    def change_french(self):
        if self.flip_timer:
            self.after_cancel(self.flip_timer)  # cancel old timer

        self.new_word = random.choice(word_list_dict)
        self.itemconfig(self.card_bg, image=self.card_front_img)
        self.itemconfig(self.language_text, text="French", fill="black")
        self.itemconfig(self.word_text, text=self.new_word['French'], fill="black")

        self.right_button.config(state=tk.DISABLED)
        self.wrong_button.config(state=tk.DISABLED)
        self.flip_timer = self.after(3000, self.change_english)

    def change_english(self):
        self.itemconfig(self.card_bg, image=self.card_back_img)
        self.itemconfig(self.language_text, text="English", fill="white")
        self.itemconfig(self.word_text, text=self.new_word['English'], fill="white")

        self.right_button.config(state=tk.NORMAL)
        self.wrong_button.config(state=tk.NORMAL)

    def word_known(self):
        word_list_dict.remove(self.new_word)
        self.change_french()
        print(f"Remaining words: {len(word_list_dict)}")

    def word_not_known(self):
        df2 = pandas.DataFrame(word_list_dict)
        df2.to_csv("./data/words_to_learn.csv", index=False)
        self.change_french()
