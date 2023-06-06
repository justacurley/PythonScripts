from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = self.get_score()
        self.score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0,280)
        self.update_scoreboard()

    def incr_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.highscore} ", False, "center",('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def get_score(self):
        with open("hiscore/hiscore.txt","r") as file:
            contents = file.read()
            return int(contents)

    def write_score(self):
        with open("hiscore/hiscore.txt","w") as file:
            file.write(str(self.highscore))

