from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, answer, x, y):
        self.goto(x, y)
        self.write(answer.title())
