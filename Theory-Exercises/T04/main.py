import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
from mpl_toolkits.mplot3d import Axes3D

def plot2d(x, y, u, figtitle):
    # This function yields a pretty 3D plot of a 2D field. It takes three
    # arguments: the x array of dimension (1,nx), y arrary of dim (1,ny), and
    # solution array of dimension (ny,nx)

    fig = plt.figure(figsize=(11, 7), dpi=100)
    ax = fig.add_subplot(projection='3d')
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, u, cmap=cm.inferno, rstride=2, cstride=2)
    ax.set_xlabel('$x$ [m]')
    ax.set_ylabel('$y$ [m]')
    ax.set_zlabel('$w$ [m/s]')
    ax.set_title(figtitle)
    plt.show()

def FVM(h, N, mu, dPdz, MAX, TOL, omega):
    dx = h / N
    dy = h / N
    L2norm = np.ones(1)

    ## Define initial conditions information

    w = np.zeros((N, N))
    wp1 = w.copy()
    aE = mu * dy / dx
    aW = mu * dy / dx
    aN = mu * dx / dy
    aS = mu * dx / dy
    Su = dPdz * dx * dy

    l = 0
    while (L2norm[l] > TOL):
        if (l > MAX):
            raise Exception('System not converged after MAX iterations')

        # north boundary
        aB = 2 * mu * dx / dy
        aP = aE + aW + aN + aB
        #wp1[0,1:-1] = (aE*w[0,2:] + aW*w[0,:-2] + aN*w[1,1:-1] - Su) / aP
        #wp1[0, 1:-1] = (aE * w[0, 2:] + aW * wp1[0, :-2] + aN * w[1, 1:-1] - Su) / aP
        wp1[0, 1:-1] = omega * (aE * w[0, 2:] + aW * wp1[0, :-2] + aN * w[1, 1:-1] - Su) / aP + (1 - omega) * w[0, 1:-1]

        # south boundary
        aP = aE + aW + aS + aB
        #wp1[-1,1:-1] = (aE*w[-1,2:] + aW*w[-1,:-2] + aS*w[-1,1:-1] - Su) / aP
        #wp1[-1, 1:-1] = (aE * w[-1, 2:] + aW * wp1[-1, :-2] + aS * wp1[-1, 1:-1] - Su) / aP
        wp1[-1, 1:-1] = omega * (aE * w[-1, 2:] + aW * wp1[-1, :-2] + aS * wp1[-1, 1:-1] - Su) / aP + (1 - omega) * w[-1, 1:-1]

        # west boundary
        aB = 2 * mu * dy / dx
        aP = aE + aN + aS + aB
        #wp1[1:-1,0] = (aE*w[1:-1,1] + aN*w[2:,0] + aS*w[:-2,0] - Su) / aP
        #wp1[1:-1, 0] = (aE * w[1:-1, 1] + aN * w[2:, 0] + aS * wp1[:-2, 0] - Su) / aP
        wp1[1:-1, 0] = omega * (aE * w[1:-1, 1] + aN * w[2:, 0] + aS * wp1[:-2, 0] - Su) / aP + (1 - omega) * w[1:-1, 0]

        # east boundary
        aP = aW + aN + aS + aB
        #wp1[1:-1,-1] = (aW*w[1:-1,-1] + aN*w[2:,-1] + aS*w[:-2,-1] - Su) / aP
        #wp1[1:-1, -1] = (aW * wp1[1:-1, -1] + aN * w[2:, -1] + aS * wp1[:-2, -1] - Su) / aP
        wp1[1:-1, -1] = omega * (aW * wp1[1:-1, -1] + aN * w[2:, -1] + aS * wp1[:-2, -1] - Su) / aP + (1 - omega) * w[1:-1, -1]

        # internal cells
        aP = aE + aW + aN + aS
        #wp1[1:-1,1:-1] = (aW*w[1:-1,:-2] + aE*w[1:-1,2:] + aN*w[2:,1:-1] + aS*w[:-2,1:-1] - Su) / aP
        #wp1[1:-1, 1:-1] = (aW * wp1[1:-1, :-2] + aE * w[1:-1, 2:] + aN * w[2:, 1:-1] + aS * wp1[:-2, 1:-1] - Su) / aP
        wp1[1:-1, 1:-1] = omega * (aW * wp1[1:-1, :-2] + aE * w[1:-1, 2:] + aN * w[2:, 1:-1] + aS * wp1[:-2, 1:-1] - Su) / aP + (1 - omega) * w[1:-1, 1:-1]

        # fill in corner cells as the mean of adjacent cells
        wp1[0, 0] = 0.5 * (wp1[1, 0] + wp1[0, 1])
        wp1[-1, 0] = 0.5 * (wp1[-2, 0] + wp1[-1, 1])
        wp1[0, -1] = 0.5 * (wp1[0, -2] + wp1[1, -1])
        wp1[-1, -1] = 0.5 * (wp1[-1, -2] + wp1[-2, -1])

        # compute residual L2 norm
        L2norm = np.append(L2norm, (np.sum((w - wp1) ** 2)) ** 0.5)

        w = wp1.copy()
        l += 1
    return w, L2norm

# starting time
start = time.time()

# Domain length
h = 0.1
mu = 1E-3
dPdz = -3.2
MAX = 50000
TOL = 1e-3
omega = 0.1
N = np.linspace(10,80,10)
N = N.astype(int)
wmax = np.zeros(10)

for l in range(0,10):
    w,L2norm = FVM(h, N[l], mu, dPdz, MAX, TOL, omega)
    wmax[l] = w[int(N[l]/2)-1,int(N[l]/2)-1]
    print("N = ", N[l] , "wmax = ", wmax[l])

end = time.time()
# total time taken
print(f"Runtime of the program {end - start} seconds")

# Convergence history

fig = plt.figure(figsize=(4,3), dpi=100)
plt.semilogy(L2norm[1:])
plt.ylabel('$L_2$ error')
plt.xlabel('Iterations')
#plt.title('Convergence history')
plt.grid("both")
plt.show()

# Variation in the centreline velocity with N

fig = plt.figure(figsize=(4,3), dpi=100)
plt.plot(N,wmax)
plt.ylabel('$w_{max}$ (m/s)')
plt.xlabel('Number of cells, $N$')
plt.grid("both")
plt.show()

# Plot the velocity contour

plot2d(np.linspace(0,h,N[-1]),np.linspace(0,h,N[-1]),w,'2D diffusion equation')

# Validation against analytical results

y = np.linspace(0,h,N[-1])
w_analytical = 1/(4*mu)*dPdz*(y**2 - y*h)

#fig = plt.figure(figsize=(4,3), dpi=100)
plt.plot(y,w[int(N[-1]/2),:], label='CFD')
plt.plot(y,w_analytical, label='Analytical')
plt.ylabel('$w_{max}$ [m/s]')
plt.xlabel('$y$ [m]')
plt.grid(which='both')
#plt.title('Velocity profile at $x = h/2$')
plt.legend()
plt.show()

# 2-D contour

plt.contourf(np.linspace(0,h,N[-1]), np.linspace(0,h,N[-1]), w, 500, cmap='inferno')
plt.colorbar(label = '$w$ [m/s]', ticks = np.linspace(0, min(wmax), 10))
plt.ylabel('$y$ [m]')
plt.xlabel('$x$ [m]')
plt.show()
