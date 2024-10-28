import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ",
                              prompt="what's another state's name?").title()
    # print(answer)
    # there is a method can get the x and y cor when mouse clicking
    if answer == 'Exit':
        to_learn_state = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(to_learn_state)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]  # row
        t.goto(state_data.x.item(), state_data.y.item())
        # t.write(state_data.state.item())
        t.write(answer)






