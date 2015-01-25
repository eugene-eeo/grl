from math import sqrt


def boundaries(distance, start):
    sx, sy = start
    min_x = sx - distance
    max_x = sx + distance

    min_y = sy - distance
    max_y = sy + distance

    return (min_x, max_x), (min_y, max_y)


def diagonal(distance, start, gradient):
    sx, sy = start
    for dx in range(distance):
        x = sx + dx
        y = sy + (dx * gradient)
        yield x, y


def distance(p1, p2):
    if p1 == p2:
        return 0.0
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2)**2 +
                (y1 - y2)**2)
