import pandas as pd
import matplotlib.pyplot as plt

# set directory
CFD100 = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se2/Simulation100/Python/Cp_100.xlsx")
xp100 = CFD100.parse('xp')
CFD1000 = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se2/Simulation100/Python/Cp_1000.xlsx")
xp1000 = CFD1000.parse('xp')
#FC = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se2/FC.xlsx")
#FC = FC.parse('FC')
#print(xp)


# set plot
#plt.plot(xp['x_0.02'], xp['p_0.02_2'], label='ss_lc=ps_lc=0.02; edge_lc=2 // cells=699')
#plt.plot(xp['x_0.01'], xp['p_0.01_1'], label='ss_lc=ps_lc=0.01; edge_lc=1 // cells=2522')
#plt.plot(xp['x_0.008'], xp['p_0.008_0.8'], label='ss_lc=ps_lc=0.008; edge_lc=0.8 // cells=3513')
#plt.plot(xp['x_0.007'], xp['p_0.007_0.7'], label='ss_lc=ps_lc=0.007; edge_lc=0.7 // cells=4628')
#plt.plot(xp['x_0.006'], xp['p_0.006_0.6'], label='ss_lc=ps_lc=0.006; edge_lc=0.6 // cells=5983')
#plt.plot(xp['x_0.005'], xp['p_0.005_0.5'], label='ss_lc=ps_lc=0.005; edge_lc=0.5 // cells=7685')
#plt.plot(xp['x_0.005'], xp['p_0.005_0.4'], label='ss_lc=ps_lc=0.005; edge_lc=0.4 // cells=9733')
#plt.plot(xp100['x_0.004'], xp100['p_0.004_0.4'], label='ss_lc=ps_lc=0.004; edge_lc=0.4 // cells=11406')
#plt.plot(xp['x_0.003'], xp['p_0.003_0.4'], label='ss_lc=ps_lc=0.003; edge_lc=0.4 // cells=14467')
#plt.plot(xp100['x_0.003'], xp100['p_0.003_0.3'], label='ss_lc=ps_lc=0.003; edge_lc=0.3 // cells=22871')
plt.plot(xp100['x_0.002'], xp100['p_0.002_0.3'], color='r', label='Re = 100 // cells=30841')
plt.plot(xp1000['x_0.003'], xp1000['p_0.003_0.3'], color='b', label='Re = 1000 // cells = 22871')



# set label
plt.xlabel('x/c')
plt.ylabel('pressure [Pa]')
plt.title('Pressure Distribution along the Suction and Pressure Surfaces')
#plt.title('Pressure Distribution along the Suction and Pressure Surfaces for Re=1000')
plt.legend()
plt.show()


'''

#plt.plot(xp100['time'], xp100['p_100'], color='b', label='Re = 100')
plt.plot(xp1000['time'], xp1000['p_1000'], color='b', label='Re = 1000')
#plt.axvline(x=12.5, color='r', linestyle='--', label='t = 12.5secs')
plt.axvline(x=11, linestyle='--', color='r', label='t = 11secs')


# set label
plt.xlabel('time[s]')
plt.ylabel('pressure[Pa]')
plt.title('Variation of pressure with respect to time on the selected point')
plt.legend()
plt.show()

'''
'''

# set plot
plt.plot(FC['time'], FC['Cd_100'], label='Cd @ Re=100')
plt.plot(FC['time'], FC['Cd_1000'], label='Cd @ Re=1000')
plt.plot(FC['time'], FC['Cl_100'], label='Cl @ Re=100')
plt.plot(FC['time'], FC['Cl_1000'], label='Cl @ Re=1000')


# set label
plt.xlabel('time [secs]')
plt.ylabel('Cd and Cl')
#plt.title('Pressure Distribution along the Suction and Pressure Surfaces for Re=100')
#plt.title('Pressure Distribution along the Suction and Pressure Surfaces for Re=1000')
plt.legend()
plt.show()
'''