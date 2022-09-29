import numpy as np
import matplotlib.pyplot as plt

max_k = 20000
xlen = 5.
ylen = 4.
omega = 1.5
eps_max = 0.01
#dx = 0.05
#dy = 0.05
#beta = 1
#dy = dx/beta
#nx = int(xlen/dx + 1)
#ny = int(ylen/dy + 1)

'''

print(nx, ny, xlen, ylen)
x = np.linspace(0.,xlen, nx)
y = np.linspace(0.,ylen, ny)
print(nx, ny)

'''
'''

T = np.zeros((nx,ny))
for i in range(1, nx - 1):
    T[i, 0] = 32  # lower wall = 20C
    T[i, ny - 1] = 3  # upper wall = 0C

for i in range(1, ny - 1):
    T[0, i] = 92  # left wall = 10C
    T[nx - 1, i] = 32  # right wall = 40C
#print(T)
Tkp1 = np.copy(T)


print('k','|', 'Residual')
print('------------')

'''

n = 0
it = np.zeros(6)

#for gridsize in np.linspace(0.05, 0.5, 9, endpoint= False):
#for omega in np.linspace(1.92, 1.95, 30, endpoint= False):
#for eps_max in np.linspace(0.01, 1.01, 11):
for beta in np.linspace(0.8, 1.3, 6, endpoint= True):

    dx = 0.05
    dy = dx/beta
    nx = int(xlen/dx + 1)
    ny = int(ylen/dy + 1)
    x = np.linspace(0.,xlen, nx)
    y = np.linspace(0.,ylen, ny)
    print(nx, ny)
    eps = []

    T = np.zeros((nx, ny))

    for i in range(1, nx - 1):
        T[i, 0] = 32  # lower wall = 32C
        T[i, ny - 1] = 3  # upper wall = 3C

    for i in range(1, ny - 1):
        T[0, i] = 92  # left wall = 92C
        T[nx - 1, i] = 32  # right wall = 32C

    # print(T)
    Tkp1 = np.copy(T)

    for k in range(max_k):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                # Point Jacobi method (Jacobi)
                # Tkp1[i,j] = 0.5/(1.0+beta**2) * (T[i+1,j] + T[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+T[i,j-1])

                # Point Gauss-Seidel method (PGS)
                # Tkp1[i,j] = 0.5/(1.0+beta**2) * (T[i+1,j] + Tkp1[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+Tkp1[i,j-1])

                # Point successive sver-relaxation (PSOR)
                Tkp1[i,j] = omega * 0.5 / (1.0 + beta ** 2) * (T[i+1,j] + Tkp1[i-1,j]) + (omega * 0.5 * beta ** 2) / (1.0 + beta ** 2) * (T[i,j+1] + Tkp1[i,j-1]) + (1 - omega) * T[i,j]

                # Line Gauss-Seidel method (LGS)
                # Tkp1[i,j] = 0.5/(1.0+beta**2) * (Tkp1[i+1,j] + Tkp1[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+Tkp1[i,j-1])

        # Define residual error as the cumulative difference between the computed temperature fields between subsequent iterates
        eps = np.append(eps, np.sum(np.absolute(np.subtract(Tkp1, T))))

        # Copy new temperature field to old temperature array
        T = np.copy(Tkp1)

        # Print the iteration number and residual to standard output every 25 iterations
        #if (k % 25) == 0:
            #print(k, '|', eps[k])

        # Test to see if residual error is below threshold; break if yes
        if eps[k] < eps_max:
            #print('Residual threshold reached in', k, 'iterations for eps_max = ', float("{:.2f}".format(eps_max)))
            #print('Residual threshold reached in', k, 'iterations for omega = ', float("{:.3f}".format(omega)))
            #print('Residual threshold reached in', k, 'iterations for gridsize = ', float("{:.2f}".format(gridsize)))
            print('Residual threshold reached in', k, 'iterations for beta = ', float("{:.1f}".format(beta)))
            it[n] = k
            break

    n += 1

print(it)


'''

eps = []
for k in range(max_k):
    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            # Point Jacobi method (Jacobi)
            # Tkp1[i,j] = 0.5/(1.0+beta**2) * (T[i+1,j] + T[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+T[i,j-1])

            # Point Gauss-Seidel method (PGS)
            # Tkp1[i,j] = 0.5/(1.0+beta**2) * (T[i+1,j] + Tkp1[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+Tkp1[i,j-1])

            # Point successive sver-relaxation (PSOR)
            Tkp1[i,j] = omega * 0.5 / (1.0 + beta ** 2) * (T[i+1,j] + Tkp1[i-1,j]) + (omega * 0.5 * beta ** 2) / (1.0 + beta ** 2) * (T[i,j+1] + Tkp1[i,j-1]) + (1 - omega) * T[i,j]

            # Line Gauss-Seidel method (LGS)
            # Tkp1[i,j] = 0.5/(1.0+beta**2) * (Tkp1[i+1,j] + Tkp1[i-1,j]) + (0.5*beta**2)/(1.0+beta**2) * (T[i,j+1]+Tkp1[i,j-1])

        # Define residual error as the cumulative difference between the computed temperature fields between subsequent iterates
    eps = np.append(eps, np.sum(np.absolute(np.subtract(Tkp1, T))))

    # Copy new temperature field to old temperature array
    T = np.copy(Tkp1)

    # Print the iteration number and residual to standard output every 25 iterations
    if (k % 25) == 0:
        print(k, '|', eps[k])

    # Test to see if residual error is below threshold; break if yes
    if eps[k] < eps_max:
        print('Residual threshold reached in', k, 'iterations for eps_max = ', eps_max)
        #print('Residual threshold reached in', k, 'iterations for omega = ', omega)
        break

X, Y = np.meshgrid(x,y,indexing='ij')
plt.contourf(X,Y,T,30)
cbar=plt.colorbar()
cbar.ax.set_ylabel('T ($^{\circ}$C)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(np.linspace(0,k,k+1),eps,label='PSOR')
plt.yscale('log')
plt.xlabel('Iteration')
plt.ylabel('$\epsilon$')
plt.legend()
plt.show()

'''
'''

#plot of epsilon_max vs number of iterations for PSOR
plt.plot(np.linspace(0.01, 1.01, 11), it, label='PSOR')
plt.yscale('log')
plt.xlabel('$\epsilon$')
plt.ylabel('Iteration')
plt.legend()
plt.show()

'''
'''

#plot of omega vs number of iterations for PSOR
plt.plot(np.linspace(1.92, 1.95, 30, endpoint= False), it, label='PSOR')
#plt.yscale('log')
plt.xlabel('$\omega$')
plt.ylabel('Iteration')
plt.legend()
plt.show()

'''
'''

#plot of gridsize vs number of iterations for PSOR
plt.plot(np.linspace(0.05, 0.5, 9, endpoint=False), it, label='PSOR')
#plt.yscale('log')
plt.xlabel('gridsize')
plt.ylabel('Iteration')
plt.legend()
plt.show()

'''


#plot of beta vs number of iterations for PSOR
plt.plot(np.linspace(0.8, 1.3, 6, endpoint=True), it, label='PSOR')
#plt.yscale('log')
plt.xlabel('\u03B2')
plt.ylabel('Iteration')
plt.legend()
plt.show()
