def limit(value, minimum, maximum):
    if value < minimum:
        return minimum
    elif value > maximum:
        return maximum
    else:
        return value


def center(big: float, small: float) -> float:
    return (big - small) / 2


def linear_interpolation(value, x0, x1, y0, y1):
    return y0 + (y1 - y0) * (value - x0) / (x1 - x0)
