import pandas as pd
import matplotlib.pyplot as plt
'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se5/Data.xlsx")
parsedfile = file.parse('Q1_1')

# set plot
plt.plot(parsedfile['U/U0_KE'], parsedfile['y/h'], color='b', label='k-Epsilon')
plt.plot(parsedfile['U/U0_KO'], parsedfile['y/h'], color='r', label='k-Omega')
plt.plot(parsedfile['U/U0_SA'], parsedfile['y/h'], color='c', label='Spalart-Allmaras')
plt.plot(parsedfile['U/U0_SST'], parsedfile['y/h'], color='g', label='k-Omega SST')
plt.scatter(parsedfile['U/U0'], parsedfile['ye'], color='k', label='Pitz & Daily (1983)')

# set label
plt.xlabel('$U/U_0$', fontsize=15)
plt.ylabel('$y/h$', fontsize=15)
plt.xlim([0, 1.2])
#plt.ylim([-3.5, 1])
plt.grid()
plt.legend()
plt.show()
'''
'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se5/Data.xlsx")
parsedfile = file.parse('Q1_2')

# set plot
plt.plot(parsedfile['U/U0_KE'], parsedfile['y/h'], color='b', label='k-Epsilon')
plt.plot(parsedfile['U/U0_KO'], parsedfile['y/h'], color='r', label='k-Omega')
plt.plot(parsedfile['U/U0_SA'], parsedfile['y/h'], color='c', label='Spalart-Allmaras')
plt.plot(parsedfile['U/U0_SST'], parsedfile['y/h'], color='g', label='k-Omega SST')
plt.scatter(parsedfile['U/U0'], parsedfile['ye'], color='k', label='Pitz & Daily (1983)')

# set label
plt.xlabel('$U/U_0$', fontsize=15)
plt.ylabel('$y/h$', fontsize=15)
plt.xlim([-0.4, 1.2])
#plt.ylim([-1.25, 1.25])
plt.grid()
plt.legend()
plt.show()
'''
'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se5/Data.xlsx")
parsedfile = file.parse('Q2')

# set plot
plt.plot(parsedfile['x/h'], parsedfile['Cf_KE'], color='b', label='k-Epsilon')
plt.plot(parsedfile['x/h'], parsedfile['Cf_KO'], color='r', label='k-Omega')
plt.plot(parsedfile['x/h'], parsedfile['Cf_SA'], color='c', label='Spalart-Allmaras')
plt.plot(parsedfile['x/h'], parsedfile['Cf_SST'], color='g', label='k-Omega SST')
plt.axvline(x=7, linestyle='--', color='k')
plt.axhline(y=0, linestyle='--', color='k')

# set label
plt.xlabel('$x/h$', fontsize=15)
plt.ylabel(r'$C_f \times 10^3$', fontsize=15)
plt.xlim([0, 8])
plt.ylim([-3.5, 1])
plt.grid()
plt.legend()
plt.show()
'''

# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se5/Data.xlsx")
parsedfile = file.parse('Q3')

# set plot
#plt.plot(parsedfile['E'], parsedfile['xr/h1'], color='b', label='k-Epsilon')
#plt.plot(parsedfile['k1'], parsedfile['xr/h2'], color='b', label='k-Epsilon')
plt.plot(parsedfile['W'], parsedfile['xr/h5'], color='b', label='SST')
#plt.plot(parsedfile['k2'], parsedfile['xr/h4'], color='b', label='SST')
#plt.plot(parsedfile['nuTilda2'], parsedfile['xr/h6'], color='b', label='Spalart-Allmaras')


# set label
#plt.xlabel(r'$\epsilon$', fontsize=15)
plt.xlabel(r'$\omega$', fontsize=15)
#plt.xlabel('$k$', fontsize=15)
#plt.xlabel(r'$\tilde{\nu}$', fontsize=15)
plt.ylabel('$x_r/h$', fontsize=15)
#plt.xlim([0, 8])
#plt.ylim([-3.5, 1])
plt.grid()
plt.legend()
plt.show()
