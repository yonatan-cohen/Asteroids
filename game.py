import random
import turtle
from spaceship import Spaceship
from asteroid import Asteroid
from collision_detection import collision_detection


if __name__ == "__main__":
    turtle.bgcolor('black')
    screen = turtle.Screen()
    screen.tracer(0, 0)
    screen.title("Spaceship Astroids Battle")

    ship = Spaceship()
    asteroids = list()

    def activate():
        if not ship.active:
            ship.activate(True)
            turtle.clear()
            turtle.hideturtle()

    def animate():
        for b in ship.bullets:
            if b.alive:
                b.move()
                b.draw()

        for a in asteroids:
            a.move(1 / 20)
            a.draw()

        collision_detection(bullets=ship.bullets, asteroids=asteroids)

        screen.update()
        screen.ontimer(animate, 50)

    num_asteroids = 5
    screen_width, screen_height = turtle.screensize()
    x_initial_bound = screen_width
    y_initial_bound = screen_height
    for _ in range(num_asteroids):
        a = Asteroid(size=random.randint(30, 60),
                     x=random.uniform(-x_initial_bound, x_initial_bound),
                     y=random.uniform(0, screen_height),
                     speed=30)
        asteroids.append(a)

    screen.onkey(ship.left, 'Left')  # arrow left key
    screen.onkey(ship.right, 'Right')  # arrow right key
    screen.onkey(ship.fire, 'space')  # space key
    screen.onkey(activate, 's')
    style = ('Courier', 15, 'normal')
    turtle.color("White")
    turtle.write('Press s to start', font=style, align='center')
    screen.listen()  # focus on screen to collect key-events

    animate()

    screen.mainloop()
