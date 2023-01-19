import numpy as np
import matplotlib.pyplot as plt

# Define system properties
m = 1.0 # mass of the block (kg)
k = 1000.0 # spring constant (N/m)
u = 0.4 # coefficient of sliding friction (N/m/s)
alpha = 60.0 # damping coefficient (1/m)
x0 = 0.1 # initial position of the block (m)
v0 = 0.0 # initial velocity of the block (m/s)
dt = 0.01 # time step (s)
t_max = 10 # maximum time (s)

# Initialize the position and velocity arrays
x = [x0]
v = [v0]
t = [0]

# Define the time-stepping function
for i in range(int(t_max/dt)):
    a = -k*x[-1] - u*np.sign(v[-1]) - alpha*v[-1]
    v.append(v[-1] + a*dt)
    x.append(x[-1] + v[-1]*dt)
    t.append(t[-1] + dt)

# Plot the position and velocity
plt.figure(figsize = [10,5])
plt.subplot(1,2,1)
plt.plot(t, x)
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.subplot(1,2,2)
plt.plot(t, v)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

