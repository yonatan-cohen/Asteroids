import os
import turtle
from bullet import Bullet

screen = turtle.Screen()


class Spaceship():
    speed = 5

    '''
    The Spaceship moves horisontally at the bottom of the window (using the arrow keys: 'Left', 'Right')

    The Spaceship fires when the 'Space' key is pressed
    '''

    def __init__(self):
        self.turtle = turtle.Turtle()
        shape = os.path.join('images', 'ship.gif')
        turtle.addshape(shape)
        self.turtle.shape(shape)
        self.activate(False)

    def activate(self, active):
        self.active = active

        _, screen_height = turtle.screensize()
        self.x = 0
        self.y = -screen_height

        self.bullets = list()
        self.bullets.append(Bullet())

        if not active:
            self.turtle.hideturtle()
            return

        self.turtle.up()
        self.turtle.setposition(self.x, self.y)
        self.turtle.showturtle()

    def left(self):
        if not self.active:
            return
        self.x -= Spaceship.speed
        if abs(self.x) > turtle.window_width() / 2:
            self.x = self.x + turtle.window_width()
        self.turtle.penup()
        self.turtle.setposition(self.x, self.y)

    def right(self):
        if not self.active:
            return
        self.x += Spaceship.speed
        if abs(self.x) > turtle.window_width() / 2:
            self.x = self.x - turtle.window_width()
        self.turtle.penup()
        self.turtle.setpos((self.x, self.y))

    def fire(self):
        if not self.active:
            return
        add_bullet = True
        for b in self.bullets:
            if not b.alive:
                add_bullet = False
                break

        if add_bullet:
            b = Bullet()
            self.bullets.append(b)

        b.fire(x=self.x, y=self.y)


# TEST
if __name__ == "__main__":
    ship = Spaceship()

    screen.onkey(ship.left, 'Left')  # arrow left key
    screen.onkey(ship.right, 'Right')  # arrow right key
    screen.onkey(ship.fire, 'space')  # space key

    screen.listen()  # focus on screen to collect key-events

    def animate():
        for b in ship.bullets:
            if b.alive:
                b.move()
                b.draw()

        screen.update()
        screen.ontimer(animate, 50)

    screen.tracer(0, 0)
    animate()
    screen.mainloop()
