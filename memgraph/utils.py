from math import ceil


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
    middle = height // 2

    min_x = sx - distance
    min_y = sy - distance

    width = 1
    elems = [(min_x + dx) for dx in range(height)]
    mid = len(elems) // 2

    for dy in range(height):
        y = min_y + dy
        yield elems[mid], y

        blocks = int((width - 1) / 2)
        for delta in range(1, blocks + 1):
            yield elems[mid+delta], y
            yield elems[mid-delta], y

        if (dy + 1) > middle:
            width -= 2
            continue
        width += 2
