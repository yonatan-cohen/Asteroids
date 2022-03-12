import turtle
from point_in_polygon import is_point_in_polygon
from asteroid import Asteroid
from explosion import Explosion

screen = turtle.Screen()

style = ('Courier', 15, 'normal')


def collision_detection(bullets, asteroids):
    dead_asteroids, dead_bullets = list(), list()
    if not len(asteroids):
        turtle.write('You Win', font=style, align='center')
        return
    for i in range(len(bullets)):
        point = (bullets[i].x, bullets[i].y)
        for j in range(len(asteroids)):
            if asteroids[j] in dead_asteroids:
                break
            if is_point_in_polygon(point, asteroids[j].polygon):
                dead_asteroids.append(asteroids[j])
                dead_bullets.append(bullets[i])
                break
    for a in dead_asteroids:
        if a.size > 20:
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
            asteroids.append(Asteroid(a.size / 3, a.x, a.y, a.speed + 25))
        else:
            exp = Explosion(a.x, a.y)
            exp.explode()
        a.turtle.clear()
        asteroids.remove(a)

    for b in dead_bullets:
        b.turtle.clear()
        bullets.remove(b)
