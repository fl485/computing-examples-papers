import matplotlib.pyplot as plt
import numpy as np

def x_iterative(m, k, dt, n, f):
    xiter = [0.01+f/k, 0.01+f/k]
    for t in range(n-2):
        x1 = 2*xiter[-1] - xiter[-2] - (k * dt**2 / m) * xiter[-1] + (f * dt**2 / m) 
        xiter.append(x1)
    return xiter

if __name__ == "__main__":
    m = 1
    k = 40
    dt = 0.01
    n  = 2000
    f = 0 #0.025
    t_vals = [i*dt for i in range(n)]

    x_vals = x_iterative(m, k, dt, n, f)

    omega = np.sqrt(k / m)
    x_exact = [f/k + 0.01 * np.cos(omega * t) for t in t_vals]

    plt.figure(figsize=(15,6))
    plt.plot(t_vals, x_vals,  label='Finite difference', linewidth=2)
    plt.plot(t_vals, x_exact, label='Exact solution',    linewidth=1, linestyle='--', color='red')

    plt.xlabel('Time (s)')
    plt.ylabel('Displacement x(t)')
    plt.title('Spring-Mass System: $m\\ddot{x} + kx = 0$')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()