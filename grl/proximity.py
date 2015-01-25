from grl.core import boundaries, cycle


def within(point, dist, of):
    sx, sy = point
    x0, x1, y0, y1 = boundaries(dist, of)
    return (x0 <= sx <= x1 and
            y0 <= sy <= y1)


def proximity(dist, start):
    x0, x1, y0, y1 = boundaries(dist, start)
    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            yield x, y


def diamond_proximity(dist, start):
    sx, _ = start
    _, _, y0, y1 = boundaries(dist, start)

    for blocks, y in zip(cycle(dist), range(y0, y1+1)):
        for dx in range(1, blocks+1):
            yield sx+dx, y
            yield sx-dx, y
        yield sx, y
