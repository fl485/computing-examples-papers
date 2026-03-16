
def f(x):
    return x**2

def diff_f(x):
    return 2*x

def one_sided_difference(f, x, h):
    return (f(x+h) - f(x))/h

def two_sided_difference(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)

print(one_sided_difference(f,2, 0.000001))
print(two_sided_difference(f,2, 0.000001))
print(diff_f(2))