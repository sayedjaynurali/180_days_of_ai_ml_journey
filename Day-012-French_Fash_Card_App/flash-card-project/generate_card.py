from tkinter import Canvas,PhotoImage,Label,Button
import pandas
import random

bg_color = "#B1DDC6"

try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("./data/french_words.csv")
finally:
    word_list_dict = df.to_dict(orient="records")
# print(word_list_dict)

class GenerateInterface(Canvas):
    def __init__(self):
        super().__init__()
        self.config(width=800,height=526,bg=bg_color,highlightthickness=0) # Canvas
        self.card_image1 = PhotoImage(file="./images/card_front.png") # Front Card Image
        self.card_image2 = PhotoImage(file="./images/card_back.png") # Back Card Image
        self.change_french()

    def change_french(self):
        self.new_word = word_list_dict[random.randint(0,len(word_list_dict)-1)]
        self.current_card = self.create_image(400, 263, image=self.card_image1) # Current Card
        self.create_text(400,150,fill="black",font=("Ariel", 40, "italic"),text="French")
        self.create_text(400,263,fill="black",font=("Ariel", 60, "bold"),text=self.new_word['French'])
        self.grid(row=0, column=0, columnspan=2) # Positioning the Canvas
        self.after(3000,self.change_english)

    def change_english(self):
        self.current_card = self.create_image(400, 263, image=self.card_image2) # Current Card
        self.create_text(400,150,fill="black",font=("Ariel", 40, "italic"),text="English")
        self.create_text(400,263,fill="black",font=("Ariel", 60, "bold"),text=self.new_word['English'])
        self.grid(row=0, column=0, columnspan=2) # Positioning the Canvas
        self.right_img = PhotoImage(file="./images/right.png")
        self.wrong_img = PhotoImage(file="./images/wrong.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0,command=self.word_known)
        self.right_button.grid(row=1,column=0)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0,command=self.word_not_known)
        self.wrong_button.grid(row=1,column=1)

    def word_known(self):
        word_list_dict.remove(self.new_word)
        self.change_french()
        print(word_list_dict)

    def word_not_known(self):
        df2 = pandas.DataFrame(word_list_dict)
        df2.to_csv("./data/words_to_learn.csv")
