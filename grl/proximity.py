from grl.core import boundaries


def within_proximity(point, distance, start):
    sx, sy = start
    bx, by = boundaries(distance, start)
    return (bx[0] <= sx <= bx[1] and
            by[0] <= sy <= by[1])



def proximity(distance, start):
    bx, by = boundaries(distance, start)
    y0, y1 = by

    for x in range(bx[0], bx[1]+1):
        for y in range(y0, y1+1):
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
