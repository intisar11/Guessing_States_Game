import pandas
import turtle


screen = turtle.Screen()
screen.title("U.S States Game")
image = "./us-states-game-start/blank_states_img.gif"

data = pandas.read_csv("./us-states-game-start/50_states.csv")
states = data.state.to_list()

screen.addshape(image)
turtle.shape(image)
turtle.shape(image)


guess_state = []


while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 number of guesses", prompt="What's another state's name").title()

    if answer_state == 'Exit':
        break

    if answer_state in states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

missed_states = []
for state in states:
    if state not in guess_state:
        missed_states.append(state)
print(missed_states)
















