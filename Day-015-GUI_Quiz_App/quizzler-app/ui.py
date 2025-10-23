from tkinter import *
from quiz_brain import QuizBrain
import time # Not strictly used with window.after, but good to keep if you used it before

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        
        # Changed this to be an attribute we can update
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text="This is a sample Text", 
            font=("Arial", 20, "italic"), 
            fill=THEME_COLOR,  # Changed fill to match theme
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50) # Added padding
        
        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        
        # Added border=0 to make buttons look cleaner
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed, border=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed, border=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question() # Renamed this method

        self.window.mainloop()

    def get_next_question(self):
        # Reset canvas color to white at the start of getting a new question
        self.canvas.config(bg="white")
        # Ensure buttons are re-enabled if they were disabled at quiz end
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        
        if self.quiz.still_has_questions():
            # Update score label
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Get next question text
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # End of quiz
            self.canvas.itemconfig(self.question_text, 
                                   text=f"You've completed the quiz!\n\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            # Disable buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # Disable buttons temporarily to prevent multiple clicks during feedback
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)
    
    def false_pressed(self):
        # Disable buttons temporarily to prevent multiple clicks during feedback
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)
    
    def give_feedback(self, is_correct: bool):
        if is_correct:
            # Change to green for correct answer
            self.canvas.config(bg="green")
        else:
            # Change to red for wrong answer
            self.canvas.config(bg="red")
        
        # Wait 1000ms (1 sec) before getting the next question
        # This allows the user to see the feedback color
        self.window.after(1000, self.get_next_question)