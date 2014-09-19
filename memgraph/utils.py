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
    mid_height = distance + 1

    min_x = sx - distance
    min_y = sy - distance

    cx = min_x + (mid_height - 1)

    blocks = 1
    for dy in range(height):
        y = min_y + dy
        yield cx, y

        for delta in range(1, blocks):
            yield (cx + delta), y
            yield (cx - delta), y

        if (dy + 1) >= mid_height:
            blocks -= 1
            continue
        blocks += 1
