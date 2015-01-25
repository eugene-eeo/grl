from math import sqrt


def proximity(distance, start):
    sx, sy = start
    height = width = 1 + (2 * distance)

    min_x = sx - distance
    min_y = sy - distance

    for dx in range(width):
        x = min_x + dx
        for dy in range(height):
            y = min_y + dy
            yield x, y


def diagonal(distance, start, gradient):
    sx, sy = start
    for dx in range(distance):
        x = sx + dx
        y = sy + (dx * gradient)
        yield x, y


def diamond_proximity(distance, start):
    sx, sy = start
    height = 1 + (2 * distance)
    min_y = sy - distance

    blocks = 1
    for dy in range(height):
        y = min_y + dy
        yield sx, y

        for delta in range(1, blocks):
            yield (sx + delta), y
            yield (sx - delta), y

        if dy >= distance:
            blocks -= 1
            continue
        blocks += 1


def distance(p1, p2):
    if p1 == p2:
        return 0.0
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1 - x2)**2 +
                (y1 - y2)**2)
