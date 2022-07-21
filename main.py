import turtle
import pandas as pd
from state_writer import StateWriter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = StateWriter()

df = pd.read_csv("50_states.csv")
states_list = df["state"].to_list()
states_list = [state.lower() for state in states_list]

game_is_on = True
lives = 10
states_count = 0
while game_is_on:
    if states_count == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="Guess a states name?").lower()
    else:
        answer_state = screen.textinput(title=f"{states_count}/50 States Correct", prompt="What's another state's name?").lower()

    if answer_state == 'exit':
        game_is_on = False

    if answer_state in states_list:
        state_x = int(df[df["state"] == answer_state.title()]['x'])
        state_y = int(df[df["state"] == answer_state.title()]['y'])
        writer.write_state(answer_state, state_x, state_y)
        states_count += 1

    if lives == 0 or states_count == 50:
        game_is_on = False
