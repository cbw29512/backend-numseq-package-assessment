def square(n):
    """
    Returns the nth term of the numbers that can be arranged into square geometric shapes `[1, 4, 9, 16, 25 ... ]`
    """
    return n**2


def triangle(n):
    """
    Returns the nth term of the numbers that can be arranged in triangular geometric shapes `[1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... ]`
    """
    return n*(n+1)/2


def cube(n):
    """
    Returns the nth term of the numbers that can be arranged as symmetric cube shapes `[1, 8, 27, 64 ...]`
    """
    return n**3
