import turtle
import math
import random


class Asteroid:
    polygon_sides = 12  # number of polygon sides

    '''
    Parameters:
        size:   size of the asteroid
        x:      asteroid initial x position
        y:      asteroid initial y position
        speed:  asteroid speed
    '''

    def __init__(self, size, x, y, speed=30):

        # initial asteroid position
        self.x = x
        self.y = y

        # polygon size
        self.size = size

        # polygon speed
        self.speed = speed

        # initial polygon tilt (rotating, modified in each move)
        self.tilt = 0

        self.polygon = list()

        # polygon moving direction
        self.init_random_values()

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.color("blue")
        self.turtle.speed(0)

    def init_random_values(self):
        # polygon moving direction (angle, restriced down)
        self.direction = random.uniform(-math.pi, 0)

        # random amount for modifying the tilt
        self.tilt_change = random.uniform(-0.1, 0.1)

        # different sides length
        self.sides = list()
        for _ in range(Asteroid.polygon_sides):
            self.sides.append(random.uniform(0.5 * self.size, self.size))

    def move(self, t):
        '''
        t:  throttle
        '''
        # move asteroid in direction
        self.x += self.speed * t * math.cos(self.direction)
        self.y += self.speed * t * math.sin(self.direction)
        self.tilt += self.tilt_change

        screen_width, screen_height = turtle.screensize()

        if self.x > screen_width:
            self.x = -screen_width
            self.init_random_values()

        if self.x < -screen_width:
            self.x = screen_width
            self.init_random_values()

        if self.y > screen_height:
            self.y = -screen_height
            self.init_random_values()

        if self.y < -screen_height:
            self.y = screen_height
            self.init_random_values()

    def draw(self):
        self.turtle.clear()

        # polygon starting vertex
        self.polygon.clear()
        self.turtle.up()
        first_vertex = (self.x, self.y)
        self.polygon.append(first_vertex)
        self.turtle.goto(first_vertex)
        self.turtle.down()

        # align angle to the next vertex with tilt (0 degrees relative to tilt)
        angle = self.tilt

        # draw the polygon
        for i in range(Asteroid.polygon_sides):
            # angle to next vertex (360 degrees / #sides)
            angle += 2 * math.pi / Asteroid.polygon_sides

            # goto next vertex
            px = self.x + self.sides[i] * math.cos(angle)
            py = self.y + self.sides[i] * math.sin(angle)
            self.polygon.append((px, py))
            self.turtle.goto(px, py)

        # goto first vertex (close polygon)
        self.polygon.append(first_vertex)
        self.turtle.goto(first_vertex)


# TEST
if __name__ == '__main__':
    screen = turtle.Screen()

    asteroids = list()
    num_asteroids = 3
    screen_width, screen_height = turtle.screensize()
    x_initial_bound = screen_width
    y_initial_bound = screen_height
    for _ in range(num_asteroids):
        a = Asteroid(size=random.randint(30, 60),
                     x=random.uniform(0, x_initial_bound),
                     y=screen_height)
        asteroids.append(a)

    def animate():
        for a in asteroids:
            a.move(1 / 20)
            a.draw()
        turtle.update()
        screen.ontimer(animate, 50)

    screen.tracer(0, 0)
    animate()
    screen.mainloop()
