from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        # display score board on top
        self.score=0
        self.color("white")
        self.penup()
        self.goto(-50,260)
        self.hideturtle()
        self.refresh_scoreboard()
    def refresh_scoreboard(self):
        # update scoreboard
        self.write(f"Score : {self.score}", align= "left", font= ("Courier", 20, "normal"))

    def game_over(self):
        # display message for game over
        self.goto(0,0)
        self.write("GAME OVER!",align="center", font=("Courier", 20, "normal"))

    def update(self):
        # update score and clear previous screen
        self.score += 1
        self.clear()
        self.refresh_scoreboard()



