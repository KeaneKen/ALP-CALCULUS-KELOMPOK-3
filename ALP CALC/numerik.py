import numpy as np

def forward_difference(f, x, h=1e-5):
    """
    Menghitung turunan pertama f(x) menggunakan metode Forward Difference.

    Parameter:
    - f : fungsi yang ingin diturunkan (contoh: lambda x: x**2)
    - x : titik x untuk menghitung turunan
    - h : langkah (delta x), default 1e-5

    Return:
    - Aproksimasi f'(x)

    Contoh:
    >>> forward_difference(lambda x: x**2, 2)
    4.00001
    """
    return (f(x + h) - f(x)) / h


def central_difference(f, x, h=1e-5):
    """
    Menghitung turunan pertama f(x) menggunakan metode Central Difference.

    Parameter:
    - f : fungsi yang ingin diturunkan
    - x : titik x untuk menghitung turunan
    - h : langkah (delta x), default 1e-5

    Return:
    - Aproksimasi f'(x)

    Contoh:
    >>> central_difference(lambda x: x**2, 2)
    4.000000000026205
    """
    return (f(x + h) - f(x - h)) / (2 * h)


def trapezoidal(f, a, b, n=100):
    """
    Menghitung integral tentu dari f(x) pada interval [a, b] menggunakan metode Trapezoidal.

    Parameter:
    - f : fungsi yang ingin diintegralkan
    - a : batas bawah
    - b : batas atas
    - n : jumlah subinterval (semakin besar semakin akurat)

    Return:
    - Aproksimasi nilai integral

    Contoh:
    >>> trapezoidal(lambda x: x**2, 0, 1, 100)
    0.33335
    """
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


def simpsons_one_third(f, a, b, n=100):
    """
    Menghitung integral tentu dari f(x) pada interval [a, b] menggunakan metode Simpson’s 1/3.

    Parameter:
    - f : fungsi yang ingin diintegralkan
    - a : batas bawah
    - b : batas atas
    - n : jumlah subinterval (harus genap)

    Return:
    - Aproksimasi nilai integral

    Contoh:
    >>> simpsons_one_third(lambda x: x**2, 0, 1, 100)
    0.3333333333333333
    """
    if n % 2 == 1:
        n += 1  # Simpson's 1/3 butuh n genap
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        coef = 4 if i % 2 == 1 else 2
        result += coef * f(a + i * h)

    return result * h / 3
