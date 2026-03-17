import numpy as np
import matplotlib.pyplot as plt

T = 1.0
N = 10000
dt = T / N
t = np.linspace(0, T, N + 1)

dB = np.sqrt(dt) * np.random.randn(N)
B = np.concatenate(([0], np.cumsum(dB)))
integrand = np.sign(B[:-1])

Y = np.concatenate(([0], np.cumsum(integrand * dB)))

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(t, abs(B), label=r'$|B_t|$', alpha=0.7)
plt.plot(t, Y, label=r'$\int_0^t sgn(B_s)dB_s$', linewidth=2)
plt.title("Simulation of $\int_0^t sgn(B_s)dB_s$ against $|B_t|$")

plt.legend()
plt.grid(True)
plt.show()
