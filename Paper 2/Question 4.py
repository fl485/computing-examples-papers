import numpy as np


def f(x):
    return x**2 * np.sin(x**2)

def diff_f(x):
    return 2*x*np.sin(x**2) + x**2 *2*x*np.cos(x**2)

def step_method(f, x, h):
    return (f(x+h*1j)/h).imag

for h in [10**-9, 10**-12,10**-15]:
    for x in [10, 100, 1000, 10000]:
        print( 'for', h, x, 'error = ', step_method(f, x, h) - diff_f(x))


