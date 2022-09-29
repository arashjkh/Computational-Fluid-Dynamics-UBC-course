import numpy as np
import matplotlib.pyplot as plt
import math
import time
'''
### Question 1 ###

nu = 0.5       # CFL number
dt = 0.01      # time step
T = 500        # max number of time steps
u_max = 1.31   # max velocity
dx = dt * u_max / nu     # space step
L = 2 * math.pi  # domain length

# Define space vector
x = np.linspace(0, L, math.ceil(L/dx))
dx = x[1] - x[0]
print('Step size =', dx, 's')
nx = x.size
print('Number of x nodes =', nx)

# Define initial conditions
u0 = np.sin(x) + 0.5 * np.sin(0.5*x)
u = np.copy(u0)
unp1 = np.zeros(u.size)
ustar = np.zeros(u.size)
'''
'''
## Lax method

# starting time
start = time.time()
for t in range(0, T): # from 0 to T - 1
    # first node
    unp1[0] = 0.5 * (u[1] + u[nx - 2]) - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2) # 0 and nx - 1 are identical
    # middle nodes
    for i in range(1, nx - 1): # from 1 to nx - 2
        unp1[i] = 0.5 * (u[i + 1] + u[i - 1]) - 0.25 * nu * (u[i + 1] ** 2 - u[i - 1] ** 2)
    # last node
    unp1[i + 1] = 0.5*(u[1]+u[i]) - 0.25*nu*(u[1]**2 - u[i]**2)
    if t * dt == 0 or t * dt == 1 or t * dt == 3:
        string = '$t =$' + str(t * dt) + ' [s]'
        plt.plot(x, u, label=string)

    u = np.copy(unp1)

uL = np.copy(u)

end = time.time()

# total time taken
print(f"Runtime of the program for Lax method is {end - start} seconds")

string = '$t =$' + str((t + 1) * dt) + ' [s]'
plt.plot(x, u, label=string)
plt.xlabel('$x$ [m]')
plt.ylabel('$u$ [m/s]')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
'''
'''
# starting time
start = time.time()

## Lax-Wendroff method
u = np.copy(u0)
for t in range(0, T):
    # first node
    Ajp = 0.5 * (u[0] + u[1])
    Ajm = 0.5 * (u[0] + u[nx - 2])
    unp1[0] = u[0] - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2) \
              + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[1] ** 2 - u[0] ** 2) \
                                   - 0.5 * Ajm * (u[0] ** 2 - u[nx - 2] ** 2))
    # middle nodes
    for i in range(1, nx - 1):
        Ajp = 0.5 * (u[i] + u[i + 1])
        Ajm = 0.5 * (u[i] + u[i - 1])
        unp1[i] = u[i] - 0.25 * nu * (u[i + 1] ** 2 - u[i - 1] ** 2) \
                  + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[i + 1] ** 2 - u[i] ** 2) \
                                       - 0.5 * Ajm * (u[i] ** 2 - u[i - 1] ** 2)
                                       )
    # last node
    Ajp = 0.5 * (u[nx - 1] + u[1])
    Ajm = 0.5 * (u[nx - 1] + u[nx - 2])
    unp1[nx - 1] = u[nx - 1] - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2) \
              + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[1] ** 2 - u[nx - 1] ** 2) \
                                   - 0.5 * Ajm * (u[nx - 1] ** 2 - u[nx - 2] ** 2))

    if t * dt == 0 or t * dt == 1 or t * dt == 3:
        string = '$t =$' + str(t * dt) + ' [s]'
        plt.plot(x, u, label=string)

    u = np.copy(unp1)

uLW = np.copy(u)

end = time.time()

# total time taken
print(f"Runtime of the program for Lax-Wendroff is {end - start} seconds")

string = '$t =$' + str((t + 1) * dt) + ' [s]'
plt.plot(x, u, label=string)
plt.xlabel('$x$ [m]')
plt.ylabel('$u$ [m/s]')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
'''
'''
# starting time
start = time.time()

## MacCormack method
u = np.copy(u0)
for t in range(0, T):
    if (t % 2 == 0):  # even time; use forward for predictor, backward for corrector
        # forwards predictor step
        for i in range(0, nx - 1):
            ustar[i] = u[i] - 0.5 * nu * (u[i + 1] ** 2 - u[i] ** 2)
        ustar[nx - 1] = u[nx - 1] - 0.5 * nu * (u[1] ** 2 - u[nx - 1] ** 2)

        # backwards corrector step
        unp1[0] = 0.5 * (u[0] + ustar[0] - 0.5 * nu * (ustar[0] ** 2 - ustar[nx - 2] ** 2))
        for i in range(1, nx):
            unp1[i] = 0.5 * (u[i] + ustar[i] - 0.5 * nu * (ustar[i] ** 2 - ustar[i - 1] ** 2))

    else:  # odd time; use backward for predictor, forward for corrector
        # backwards predictor step
        ustar[0] = u[0] - 0.5 * nu * (u[0] ** 2 - u[nx - 2] ** 2)
        for i in range(1, nx):
            ustar[i] = u[i] - 0.5 * nu * (u[i] ** 2 - u[i - 1] ** 2)

        # forwards corrector
        for i in range(0, nx - 1):
            unp1[i] = 0.5 * (u[i] + ustar[i] - 0.5 * nu * (ustar[i + 1] ** 2 - ustar[i] ** 2))
        unp1[nx - 1] = 0.5 * (u[nx - 1] + ustar[nx - 1] - 0.5 * nu * (ustar[1] ** 2 - ustar[nx - 1] ** 2))

    if t * dt == 0 or t * dt == 1 or t * dt == 3:
        string = '$t =$' + str(t * dt) + ' [s]'
        plt.plot(x, u, label=string)

    u = np.copy(unp1)

uM = np.copy(u)

end = time.time()

# total time taken
print(f"Runtime of the program for MacCormack method is {end - start} seconds")

string = '$t =$' + str((t + 1) * dt) + ' [s]'
plt.plot(x, u, label=string)
plt.xlabel('$x$ [m]')
plt.ylabel('$u$ [m/s]')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
'''
'''
### Question 2 ###

plt.plot(x,u0,label='u(x,0)')
plt.plot(x,uL,label='Lax')
plt.plot(x,uLW,label='Lax-Wendroff')
plt.plot(x,uM,label='MacCormack')
plt.xlabel('$x$ [m]')
plt.ylabel('$u$ [m/s]')
plt.legend(loc='lower left')
plt.title('Solution at $t$ = 5 [s]')
plt.show()
'''
'''
### Question 3 ###

## Lax method
for nu in np.linspace(0.04, 0.94, 10):
    dt = 0.01  # time step
    T = 500  # max number of time steps
    u_max = 1.31
    dx = dt * u_max / nu  # space step
    L = 2 * math.pi  # domain length

    # Define space vector
    x = np.linspace(0, L, math.ceil(L / dx))
    dx = x[1] - x[0]
    print('Step size =', dx, 's')
    nx = x.size
    print('Number of x nodes =', nx)

    # Define initial conditions
    u0 = np.sin(x) + 0.5 * np.sin(0.5 * x)
    u = np.copy(u0)
    unp1 = np.zeros(u.size)

    for t in range(0, T):  # from 0 to T - 1
        # first node
        unp1[0] = 0.5 * (u[1] + u[nx - 2]) - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2)  # 0 and nx - 1 are identical
        # middle nodes
        for i in range(1, nx - 1):  # from 1 to nx - 2
            unp1[i] = 0.5 * (u[i + 1] + u[i - 1]) - 0.25 * nu * (u[i + 1] ** 2 - u[i - 1] ** 2)
        # last node
        unp1[i + 1] = 0.5 * (u[1] + u[i]) - 0.25 * nu * (u[1] ** 2 - u[i] ** 2)
        u = np.copy(unp1)

    string = '$CFL =$' + str(round(nu,2))
    plt.plot(x, u, label=string)
    plt.xlabel('$x$ [m]')
    plt.ylabel('$u$ [m/s]')
    plt.title('Lax method for different Courant numbers at t = 5[s]')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
'''
'''
## Lax-Wendroff method
for nu in np.linspace(0.09, 0.79, 8):
    dt = 0.01  # time step
    T = 500  # max number of time steps
    u_max = 1.31
    dx = dt * u_max / nu  # space step
    L = 2 * math.pi  # domain length

    # Define space vector
    x = np.linspace(0, L, math.ceil(L / dx))
    dx = x[1] - x[0]
    print('Step size =', dx, 's')
    nx = x.size
    print('Number of x nodes =', nx)

    # Define initial conditions
    u0 = np.sin(x) + 0.5 * np.sin(0.5 * x)
    u = np.copy(u0)
    unp1 = np.zeros(u.size)
    for t in range(0, T):
        # first node
        Ajp = 0.5 * (u[0] + u[1])
        Ajm = 0.5 * (u[0] + u[nx - 2])
        unp1[0] = u[0] - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2) \
                  + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[1] ** 2 - u[0] ** 2) \
                                       - 0.5 * Ajm * (u[0] ** 2 - u[nx - 2] ** 2))
        # middle nodes
        for i in range(1, nx - 1):
            Ajp = 0.5 * (u[i] + u[i + 1])
            Ajm = 0.5 * (u[i] + u[i - 1])
            unp1[i] = u[i] - 0.25 * nu * (u[i + 1] ** 2 - u[i - 1] ** 2) \
                      + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[i + 1] ** 2 - u[i] ** 2) \
                                           - 0.5 * Ajm * (u[i] ** 2 - u[i - 1] ** 2)
                                           )
        # last node
        Ajp = 0.5 * (u[nx - 1] + u[1])
        Ajm = 0.5 * (u[nx - 1] + u[nx - 2])
        unp1[nx - 1] = u[nx - 1] - 0.25 * nu * (u[1] ** 2 - u[nx - 2] ** 2) \
                       + 0.5 * (nu ** 2) * (0.5 * Ajp * (u[1] ** 2 - u[nx - 1] ** 2) \
                                            - 0.5 * Ajm * (u[nx - 1] ** 2 - u[nx - 2] ** 2))
        u = np.copy(unp1)

    string = '$CFL =$' + str(round(nu,2))
    plt.plot(x, u, label=string)
    plt.xlabel('$x$ [m]')
    plt.ylabel('$u$ [m/s]')
    plt.title('Lax-Wendroff method for different Courant numbers at t = 5[s]')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
'''
'''
## MacCormack method
for nu in np.linspace(0.09, 0.79, 8):
    dt = 0.01  # time step
    T = 500  # max number of time steps
    u_max = 1.31
    dx = dt * u_max / nu  # space step
    L = 2 * math.pi  # domain length

    # Define space vector
    x = np.linspace(0, L, math.ceil(L / dx))
    dx = x[1] - x[0]
    print('Step size =', dx, 's')
    nx = x.size
    print('Number of x nodes =', nx)

    # Define initial conditions
    u0 = np.sin(x) + 0.5 * np.sin(0.5 * x)
    u = np.copy(u0)
    ustar = np.zeros(u.size)
    unp1 = np.zeros(u.size)
    ## MacCormack method
    for t in range(0, T):
        if (t % 2 == 0):  # even time; use forward for predictor, backward for corrector
            # forwards predictor step
            for i in range(0, nx - 1):
                ustar[i] = u[i] - 0.5 * nu * (u[i + 1] ** 2 - u[i] ** 2)
            ustar[nx - 1] = u[nx - 1] - 0.5 * nu * (u[1] ** 2 - u[nx - 1] ** 2)

            # backwards corrector step
            unp1[0] = 0.5 * (u[0] + ustar[0] - 0.5 * nu * (ustar[0] ** 2 - ustar[nx - 2] ** 2))
            for i in range(1, nx):
                unp1[i] = 0.5 * (u[i] + ustar[i] - 0.5 * nu * (ustar[i] ** 2 - ustar[i - 1] ** 2))

        else:  # odd time; use backward for predictor, forward for corrector
            # backwards predictor step
            ustar[0] = u[0] - 0.5 * nu * (u[0] ** 2 - u[nx - 2] ** 2)
            for i in range(1, nx):
                ustar[i] = u[i] - 0.5 * nu * (u[i] ** 2 - u[i - 1] ** 2)

            # forwards corrector
            for i in range(0, nx - 1):
                unp1[i] = 0.5 * (u[i] + ustar[i] - 0.5 * nu * (ustar[i + 1] ** 2 - ustar[i] ** 2))
            unp1[nx - 1] = 0.5 * (u[nx - 1] + ustar[nx - 1] - 0.5 * nu * (ustar[1] ** 2 - ustar[nx - 1] ** 2))

        u = np.copy(unp1)

    string = '$CFL =$' + str(round(nu,2))
    plt.plot(x, u, label=string)
    plt.xlabel('$x$ [m]')
    plt.ylabel('$u$ [m/s]')
    plt.title('MacCormack method for different Courant numbers at t = 5[s]')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.show()
'''