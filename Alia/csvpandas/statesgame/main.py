import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Games")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


counter = 0
correct_guesses = []
# Import CSV
state_data = pd.read_csv("50_states.csv")
keep_guessing = True
while keep_guessing:
    answer_state = screen.textinput(title=f"{counter}/50:Guess the State",prompt="Guess a state name")
    guess = answer_state.title()
    found_state = state_data[(state_data.state == guess)]
    if found_state.empty:
        print("dne")
    else:
        counter = counter+1
        correct_guesses.appen(found_state.state.item())
        x = int(found_state.x)
        y = int(found_state.y)
        print("exist")
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.ht()
        state_turtle.goto(x,y)
        state_turtle.write(found_state.state.item())

# Check if answer_state in csv.state

# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
screen.mainloop()
# screen.exitonclick()
# ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
