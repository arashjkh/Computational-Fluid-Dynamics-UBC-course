import pandas as pd
import matplotlib.pyplot as plt
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/velocity.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['P4'], v1['U4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')
plt.plot(v1['P3'], v1['U3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['P2'], v1['U2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['P1'], v1['U1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['P0'], v1['U0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')

# set label
plt.xlabel('r [m]')
plt.ylabel('u_z [m/s]')
#plt.title('Axial Velocity with Respect to Radius at Pipe Outlet after achieving Steady-state')
plt.legend()
plt.grid()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/pressure.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['P0'], v1['p0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')
plt.plot(v1['P1'], v1['p1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['P2'], v1['p2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['P3'], v1['p3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['P4'], v1['p4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')

# set label
plt.xlabel('z [m]')
plt.ylabel('pressure [Pa]')
#plt.title('Pressure along the Pipeline after Achieving Steady-state')
plt.legend()
plt.grid()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/velocity2.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['P0'], v1['U0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')
plt.plot(v1['P1'], v1['U1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['P2'], v1['U2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['P3'], v1['U3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['P4'], v1['U4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')

# set label
plt.xlabel('z [m]')
plt.ylabel('u_z [m/s]')
#plt.title('Quantitative Development of Axial Velocity along the Center-line of Pipeline')
plt.legend()
plt.grid()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/time2.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['time'], v1['U0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')
plt.plot(v1['time'], v1['U1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['time'], v1['U2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['time'], v1['U3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['time'], v1['U4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')
plt.axvline(x=210, linestyle='--', color='r', label='t = 210 seconds')

# set label
plt.xlabel('time [s]')
plt.ylabel('u_z [m/s]')
#plt.title('Quantitative Development of Axial Velocity of a Point at the Center of Pipeline Outlet')
plt.legend()
plt.grid()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/4/RadialVelocity/RadialVelocity.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['Points'], v1['U10'], label='t = 10[s]')
plt.plot(v1['Points'], v1['U30'], label='t = 30[s]')
plt.plot(v1['Points'], v1['U50'], label='t = 50[s]')
plt.plot(v1['Points'], v1['U70'], label='t = 70[s]')
plt.plot(v1['Points'], v1['U90'], label='t = 90[s]')
#plt.plot(v1['Points'], v1['U110'], label='t = 110[s]')
plt.plot(v1['Points'], v1['U130'], label='t = 130[s]')
#plt.plot(v1['Points'], v1['U150'], label='t = 150[s]')
plt.plot(v1['Points'], v1['U170'], label='t = 170[s]')
#plt.plot(v1['Points'], v1['U190'], label='t = 190[s]')
#plt.plot(v1['Points'], v1['U200'], label='t = 200[s]')
plt.plot(v1['Points'], v1['U210'], label='t = 210[s]')
#plt.plot(v1['Points'], v1['U230'], label='t = 230[s]')
plt.plot(v1['Points'], v1['U250'], label='t = 250[s]')

# set label
plt.xlabel('r [m]')
plt.ylabel('u_z [m/s]')
#plt.title('Quantitative Development of Velocity with Respect to Radius at Pipe Outlet in Different Times')
plt.grid()
plt.legend()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/4/PV/PV.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['Points'], v1['U10'], label='t = 10[s]')
plt.plot(v1['Points'], v1['U30'], label='t = 30[s]')
plt.plot(v1['Points'], v1['U50'], label='t = 50[s]')
plt.plot(v1['Points'], v1['U70'], label='t = 70[s]')
plt.plot(v1['Points'], v1['U90'], label='t = 90[s]')
#plt.plot(v1['Points'], v1['U110'], label='t = 110[s]')
plt.plot(v1['Points'], v1['U130'], label='t = 130[s]')
#plt.plot(v1['Points'], v1['U150'], label='t = 150[s]')
plt.plot(v1['Points'], v1['U170'], label='t = 170[s]')
#plt.plot(v1['Points'], v1['U190'], label='t = 190[s]')
#plt.plot(v1['Points'], v1['U200'], label='t = 200[s]')
plt.plot(v1['Points'], v1['U210'], label='t = 210[s]')
#plt.plot(v1['Points'], v1['U230'], label='t = 230[s]')
plt.plot(v1['Points'], v1['U250'], label='t = 250[s]')
#plt.plot(v1['Points'], v1['U1500'], label='t = 1500[s]')


# set label
plt.xlabel('z [m]')
plt.ylabel('u_z [m/s]')
#plt.title('Quantitative Development of Axial Velocity along the Center-line of Pipeline')
plt.grid()
plt.legend()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/4/PV/PV.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['Points'], v1['p10'], label='t = 10[s]')
plt.plot(v1['Points'], v1['p30'], label='t = 30[s]')
plt.plot(v1['Points'], v1['p50'], label='t = 50[s]')
plt.plot(v1['Points'], v1['p70'], label='t = 70[s]')
plt.plot(v1['Points'], v1['p90'], label='t = 90[s]')
#plt.plot(v1['Points'], v1['p110'], label='t = 110[s]')
plt.plot(v1['Points'], v1['p130'], label='t = 130[s]')
#plt.plot(v1['Points'], v1['p150'], label='t = 150[s]')
plt.plot(v1['Points'], v1['p170'], label='t = 170[s]')
#plt.plot(v1['Points'], v1['p190'], label='t = 190[s]')
#plt.plot(v1['Points'], v1['p200'], label='t = 200[s]')
plt.plot(v1['Points'], v1['p210'], label='t = 210[s]')
#plt.plot(v1['Points'], v1['p230'], label='t = 230[s]')
plt.plot(v1['Points'], v1['p250'], label='t = 250[s]')
#plt.plot(v1['Points'], v1['p1500'], label='t = 1500[s]')


# set label
plt.xlabel('z [m]')
plt.ylabel('pressure [Pa]')
#plt.title('Pressure along the Pipeline')
plt.grid()
plt.legend()
plt.show()
'''
'''
# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/5.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['P'], v1['U0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')
plt.plot(v1['P'], v1['U1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['P'], v1['U2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['P'], v1['U3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['P'], v1['U4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')
plt.plot(v1['P'], v1['Ua'], label='Analytical')

# set label
plt.xlabel('r/R')
plt.ylabel('u_z/u_z_max')
#plt.title('Axial Velocity with Respect to Radius at Pipe Outlet after achieving Steady-state')
plt.legend()
plt.grid()
plt.show()

# set plot
plt.plot(v1['P'], v1['error0'], label='(N2 N1 N3) = (6 2 10) || #cells = 520')
plt.plot(v1['P'], v1['error1'], label='(N2 N1 N3) = (15 5 25) || #cells = 8125')
plt.plot(v1['P'], v1['error2'], label='(N2 N1 N3) = (30 10 50) || #cells = 65000')
plt.plot(v1['P'], v1['error3'], label='(N2 N1 N3) = (40 15 75) || #cells = 196875')
plt.plot(v1['P'], v1['error4'], label='(N2 N1 N3) = (40 15 80) || #cells = 210000')

# set label
plt.xlabel('r/R')
plt.ylabel('Axial Velocity Relative Error')
#plt.title('Axial Velocity with Respect to Radius at Pipe Outlet after achieving Steady-state')
plt.legend()
plt.grid()
plt.show()
'''

# set directory
Velocity = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se3/velocity3.xlsx")
v1 = Velocity.parse('Sheet1')

# set plot
plt.plot(v1['P'], v1['U'], label='(N2 N1 N3) = (30 10 100) || #cells = 130000')
plt.axvline(x=29, linestyle='--', color='r', label='t = 29 [m]')

# set label
plt.xlabel('z [m]')
plt.ylabel('u_z [m/s]')
#plt.title('Axial Velocity with Respect to Radius at Pipe Outlet after achieving Steady-state')
plt.legend()
plt.grid()
plt.show()
