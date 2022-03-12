import turtle
import math
import random

screen = turtle.Screen()


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.p = []
        self.dir = []
        self.s = []
        self.t = 1
        self.turtle = turtle.Turtle()
        self.turtle.color("red")
        self.turtle.hideturtle()
        self.turtle.up()
        for _ in range(12):
            self.p.append([x, y])
            self.dir.append(random.uniform(0, math.pi * 2))
            self.s.append(random.uniform(200, 300))

    def draw(self):
        self.turtle.clear()
        if self.t > 0:
            for i in range(len(self.p)):
                self.turtle.goto(self.p[i])
                self.turtle.dot(2)

    def move(self, t):
        self.t -= t
        for i in range(len(self.p)):
            self.p[i][0] += self.s[i] * t * math.cos(self.dir[i])
            self.p[i][1] += self.s[i] * t * math.sin(self.dir[i])
            self.s[i] *= 0.9

    def explode(self):
        self.move(1/20)
        self.draw()
        if self.t > 0:
            screen.ontimer(self.explode, 50)


# TEST
if __name__ == '__main__':
    screen.tracer(0, 0)
    exp = Explosion(100, 100)
    exp.explode()
    turtle.mainloop()
