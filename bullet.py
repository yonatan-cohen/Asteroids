from audioop import add
import turtle
import random


class Bullet:
    speed = 20
    size = 5
    initial_y = 10  # fire from top of spaceship

    def __init__(self):
        self.x = 0
        self.y = 0
        self.alive = False

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.color("purple")

    def fire(self, x=0, y=0):
        self.x = x
        self.y = y + Bullet.initial_y
        self.alive = True

    def move(self):
        self.y += Bullet.speed
        if self.y > turtle.window_height() / 2:
            self.alive = False

    def draw(self):
        self.turtle.clear()
        self.turtle.goto(self.x, self.y)
        self.turtle.dot(Bullet.size)


# TEST
if __name__ == '__main__':
    screen = turtle.Screen()

    bullets = list()
    bullets.append(Bullet())

    def fire():
        add_bullet = True
        for b in bullets:
            if not b.alive:
                add_bullet = False  # use free bullet
                break

        if add_bullet:
            b = Bullet()
            bullets.append(b)

        b.fire(x=random.randint(-100, 100))

    screen.onkey(fire, 'space')
    screen.listen()

    def animate():
        for b in bullets:
            if b.alive:
                b.move()
                b.draw()
        screen.ontimer(animate, 50)

    screen.tracer(0, 0)
    animate()
    screen.mainloop()
