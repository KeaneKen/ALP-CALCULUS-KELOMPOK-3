def forward_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def trapezoidal(f, a, b, n=100):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

def simpsons_one_third(f, a, b, n=100):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        result += coef * f(a + i * h)
    return result * h / 3
