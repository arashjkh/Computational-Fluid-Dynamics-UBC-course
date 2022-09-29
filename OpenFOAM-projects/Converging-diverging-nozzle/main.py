import pandas as pd
import matplotlib.pyplot as plt
'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se4/Data1.xlsx")
parsedfile = file.parse('Sheet1')

# set plot
#plt.plot(parsedfile['P89a'], parsedfile['p89a'], linestyle='--', color='r', label='Experiment')
#plt.plot(parsedfile['P89'], parsedfile['p89'], color='b', label='CFD')
plt.plot(parsedfile['P75a'], parsedfile['p75a'], linestyle='--', color='r', label='Experiment')
plt.plot(parsedfile['P75'], parsedfile['p75'], color='b', label='CFD')
#plt.plot(parsedfile['P16a'], parsedfile['p16a'], linestyle='--', color='r', label='Experiment')
#plt.plot(parsedfile['P16'], parsedfile['p16'], color='b', label='CFD')

#plt.plot(parsedfile['P89a'], parsedfile['M89a'], linestyle='--', color='r', label='Experiment')
#plt.plot(parsedfile['P89'], parsedfile['M89'], color='b', label='CFD')
#plt.plot(parsedfile['P75a'], parsedfile['M75a'], linestyle='--', color='r', label='Experiment')
#plt.plot(parsedfile['P75'], parsedfile['M75'], color='b', label='CFD')
#plt.plot(parsedfile['P16a'], parsedfile['M16a'], linestyle='--', color='r', label='Experiment')
#plt.plot(parsedfile['P16'], parsedfile['M16'], color='b', label='CFD')


# set label
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
plt.xlabel('x [in]')
#plt.ylabel('Mach Number')
plt.ylabel('$p/p_0$')
plt.legend()
plt.grid()
plt.show()
'''

# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se4/Data1.xlsx")
parsedfile = file.parse('Sheet2')

# set plot
#plt.plot(parsedfile['Time'], parsedfile['U86'], color='b', label='p/$p_0$=0.89')
#plt.axvline(x=0.7, linestyle='--', color='r', label='t = 0.7 [s]')
#plt.plot(parsedfile['Time'], parsedfile['U75'], color='b', label='p/$p_0$=0.75')
#plt.axvline(x=0.32, linestyle='--', color='r', label='t = 0.32 [s]')
#plt.plot(parsedfile['Time'], parsedfile['U16'], color='b', label='p/$p_0$=0.16')
#plt.axvline(x=0.18, linestyle='--', color='r', label='t = 0.18 [s]')

plt.plot(parsedfile['Time'], parsedfile['U86'], color='b', label='p/$p_0$=0.89')
plt.plot(parsedfile['Time32'], parsedfile['U7532'], color='r', label='p/$p_0$=0.75')
plt.plot(parsedfile['Time18'], parsedfile['U1618'], color='g', label='p/$p_0$=0.16')

# set label
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
plt.xlabel('t [s]')
#plt.ylabel('$M$')
plt.ylabel('$V_{outlet}$ [m/s]')
plt.legend()
plt.grid()
plt.show()

'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se4/Data3.xlsx")
parsedfile = file.parse('Sheet1')

# set plot
plt.plot(parsedfile['P'], parsedfile['p'], label='Pressure [Pa]')
plt.plot(parsedfile['P'], parsedfile['Ma'], label='Mach Number')

# set label
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
plt.xlabel('x [m]')
#plt.ylabel('Mach Number')
#plt.ylabel('p [Pa]')
plt.legend()
plt.grid()
plt.show()
'''
'''
# set directory
file = pd.ExcelFile("C:/users/arashjkh/desktop/ENGR491/SoftwareExercises/se4/Data1.xlsx")
parsedfile = file.parse('Sheet3')

# set plot
plt.plot(parsedfile['P'], parsedfile['p0'], label='t = 0 [s]')
plt.plot(parsedfile['P'], parsedfile['p1'], label='t = 1 [s]')
plt.plot(parsedfile['P'], parsedfile['p2'], label='t = 2 [s]')
plt.plot(parsedfile['P'], parsedfile['p3'], label='t = 3 [s]')
plt.plot(parsedfile['P'], parsedfile['p4'], label='t = 4 [s]')
plt.plot(parsedfile['P'], parsedfile['p5'], label='t = 5 [s]')
plt.plot(parsedfile['P'], parsedfile['p6'], label='t = 6 [s]')


# set label
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
plt.xlabel('x [m]')
#plt.ylabel('$M$')
plt.ylabel('$p/p_0$')
plt.legend()
plt.grid()
plt.show()
'''