import numpy as np

def f(x):
    return x**3 + x**2

def trapezoidal_rule(function, lower, upper, n, weights):
    answer = 0
    for x in np.linspace(lower, upper, n):
        answer += function(x) * weights
    answer *= (upper - lower)
    return answer

def simpsons_rule(function, lower, upper, locations, weights):
    answer = 0
    for i, x in enumerate(locations):
        answer += function(x) * weights[i]
    answer *= (upper - lower)
    return answer

def two_point_gauss(function, lower, upper, locations, weights):
    answer = 0
    for x in locations:
        answer += function(x) * weights
    answer *= (upper - lower)
    return answer

if __name__ == "__main__":
    a = 0
    b = 10

    qa = trapezoidal_rule(f, a, b, 2, 1/2)
    print('a)', abs(qa - 8500/3))

    wsimpson = [1/6, 2/3, 1/6]
    xsimpson = [a, (a+b)/2, b]
    qb = simpsons_rule(f, a, b, xsimpson, wsimpson)
    print('b)', abs(qb - 8500/3))

    xgauss = [1/2*(a+b + (a+b)/(np.sqrt(3))), 1/2*(a+b - (a+b)/(np.sqrt(3)))]
    qc = two_point_gauss(f, a, b, xgauss, 1/2)
    print('c)', abs(qc - 8500/3))