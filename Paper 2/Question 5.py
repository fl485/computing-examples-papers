import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + np.cos(10*x)/5

interval = np.linspace(0,2*np.pi, 50)
fval = f(interval)

window = 3
moving_average=[(sum(fval[n:n+window])/window) for n in range(len(fval - window + 1))]

plt.figure(figsize=(15,6))
plt.plot(interval, fval,  label='original function')
plt.plot(interval, moving_average, label='3 point moving average')
plt.legend()
plt.grid(True)
plt.show()