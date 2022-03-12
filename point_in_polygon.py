def orientation(p1, p2, p3):
    return 1 if (p2[1] - p1[1]) * (p3[0] - p2[0]) > (p3[1] - p2[1]) * (p2[0] - p1[0]) else 2


def intersect(p1, q1, p2, q2):
    if orientation(p1, q1, p2) == orientation(p1, q1, q2) or orientation(p2, q2, p1) == orientation(p2, q2, q1):
        return False
    return True


def is_point_in_polygon(p, polygons, even=False):
    for i in range(len(polygons)):
        if intersect(p, (1000, 1000), polygons[i], polygons[(i+1) % len(polygons)]):
            even = not even
    return even
