from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global marks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text0.config(text="Timer", fg=GREEN)
    text1.config(text="")
    marks = ""
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        text0.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        text0.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        text0.config(text="Do that Shit!", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer, reps, marks

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔︎"
        text1.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text0 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
text0.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Label(text="Start", bg="white", fg="black", relief="solid", borderwidth=1, font=(FONT_NAME, 12), padx=10, pady=5)
start_button.grid(row=2, column=0)
start_button.bind("<Button-1>", lambda event: start_timer())

reset_button = Label(text="Reset", bg="white", fg="black", relief="solid", borderwidth=1, font=(FONT_NAME, 12), padx=10, pady=5)
reset_button.grid(row=2, column=2)
reset_button.bind("<Button-1>", lambda event: reset_timer())

text1 = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
text1.grid(row=3, column=1)

window.mainloop()