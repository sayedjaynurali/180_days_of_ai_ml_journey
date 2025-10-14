import turtle
import pandas

screen = turtle.Screen()
screen.tracer(0)
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim = turtle.Turtle()

states_data = pandas.read_csv("./50_states.csv")
s_dict = states_data.to_dict()
guessed_states  = []

while len(guessed_states)<len(s_dict["state"]):
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What is another state's name?").strip().title()
    if answer_state == "Exit":
        to_learn_states = {"state":[s_dict["state"][key] for key in s_dict["state"] if s_dict["state"][key] not in guessed_states]}

        df = pandas.DataFrame(to_learn_states)
        df.to_csv("./to_learn_states.csv")
        
        break

    for s_key in s_dict["state"]:
        if answer_state == s_dict["state"][s_key] and answer_state not in guessed_states:
            tim.hideturtle()
            tim.penup()
            tim.goto(s_dict["x"][s_key],s_dict["y"][s_key])
            tim.write(s_dict["state"][s_key],align="center",font=("Arial",8,"normal"))
            guessed_states.append(s_dict["state"][s_key])

screen.mainloop()