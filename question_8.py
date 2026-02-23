import numpy as np
import math


def functiona(x,y):
    return math.exp(x*y) * (math.cos(y))**2 * math.sin(x**2)

def functionb(x,y):
    return 1 if x**2 + y**2 <= 1 else 0

def monte_carlo_integration(f, lowery, uppery, lowerx, upperx, n):
    mean = 0
    area = (upperx - lowerx) * (uppery - lowery)
    for i in range(n):
        x = np.random.uniform(lowerx, upperx)
        y = np.random.uniform(lowery, uppery)
        mean += 1/n * f(x, y)
    return mean * area

if __name__ == "__main__":
    qa = monte_carlo_integration(functiona, -1, 1, -1, 1, 50000)
    print(qa)

    qb = monte_carlo_integration(functionb, -1, 1, -1, 1, 50000)
    print(qb)
