from math import sqrt


def boundaries(dist, start):
    sx, sy = start
    return (sx - dist, sx + dist,
            sy - dist, sy + dist)


def cycle(dist):
    blocks = 0
    for _ in range(dist):
        yield blocks
        blocks += 1
    yield blocks
    for _ in range(dist):
        blocks -= 1
        yield blocks


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
