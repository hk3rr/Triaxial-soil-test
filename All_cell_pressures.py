# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 19:03:29 2022

@author: hk3rr
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import interactive

"""
50kPa
"""

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2500 - Geotechnical Engineering\Spring Coursework\TX1A50.xlsx")
ExForce = pd.DataFrame(data, columns= ['Force (N)'])
Force = ExForce.to_numpy(dtype='float', na_value=np.nan)
ExStroke = pd.DataFrame(data, columns= ['Stroke (mm)'])
Stroke = ExStroke.to_numpy(dtype='float', na_value=np.nan)

l0 = 75#mm
A0mm = 1104#mm^2
A0 = A0mm/1000**2 #m^2

Strain = (Stroke/l0) * 100 #%
A = A0/(1-(Strain/100)) #m^2
Stress = (Force/A) / 1000 #kNm^-2

#Force and Displacement

plt.figure(1)
plt.plot(Stroke,Force,'blue')

plt.title("Cell 1 : 50 kPa Cell Pressure")
plt.xlabel("Axial Displacement (mm)")
plt.ylabel("Axial load (N)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

interactive(True)
plt.show()

#Axial Strain and Deviatoric Stress

plt.figure(2)
plt.plot(Strain,Stress,'blue')

plt.title("Cell 1 : 50 kPa Cell Pressure")
plt.xlabel("Axial Strain (%)")
plt.ylabel("Deviatoric Stress (kPa)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.show()

interactive(False)
plt.show()

"""
100kPa
"""

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2500 - Geotechnical Engineering\Spring Coursework\TX2A100.xlsx")
ExForce = pd.DataFrame(data, columns= ['Force (N)'])
Force = ExForce.to_numpy(dtype='float', na_value=np.nan)  
ExStroke = pd.DataFrame(data, columns= ['Stroke (mm)'])
Stroke = ExStroke.to_numpy(dtype='float', na_value=np.nan)  

l0 = 75#mm
A0mm = 1104#mm^2
A0 = A0mm/1000**2 #m^2

Strain = (Stroke/l0) * 100 #%
A = A0/(1-(Strain/100)) #m^2
Stress = (Force/A) / 1000 #kNm^-2

#Force and Displacement

plt.figure(1)
plt.plot(Stroke,Force,'blue')

plt.title("Cell 2 : 100 kPa Cell Pressure")
plt.xlabel("Axial Displacement (mm)")
plt.ylabel("Axial load (N)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

interactive(True)
plt.show()

#Axial Strain and Deviatoric Stress

plt.figure(2)
plt.plot(Strain,Stress,'blue')

plt.title("Cell 2 : 100 kPa Cell Pressure")
plt.xlabel("Axial Strain (%)")
plt.ylabel("Deviatoric Stress (kPa)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.show()

interactive(False)
plt.show()

"""
150kPa
"""

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2500 - Geotechnical Engineering\Spring Coursework\TX3A150.xlsx")
ExForce = pd.DataFrame(data, columns= ['Force (N)'])
Force = ExForce.to_numpy(dtype='float', na_value=np.nan)  
ExStroke = pd.DataFrame(data, columns= ['Stroke (mm)'])
Stroke = ExStroke.to_numpy(dtype='float', na_value=np.nan)  

l0 = 75#mm
A0mm = 1104#mm^2
A0 = A0mm/1000**2 #m^2

Strain = (Stroke/l0) * 100 #%
A = A0/(1-(Strain/100)) #m^2
Stress = (Force/A) / 1000 #kNm^-2

#Force and Displacement

plt.figure(1)
plt.plot(Stroke,Force,'blue')

plt.title("Cell 3 : 150 kPa Cell Pressure")
plt.xlabel("Axial Displacement (mm)")
plt.ylabel("Axial load (N)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

interactive(True)
plt.show()

#Axial Strain and Deviatoric Stress

plt.figure(2)
plt.plot(Strain,Stress,'blue')

plt.title("Cell 3 : 150 kPa Cell Pressure")
plt.xlabel("Axial Strain (%)")
plt.ylabel("Deviatoric Stress (kPa)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.show()

interactive(False)
plt.show()

"""
200kPa
"""

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2500 - Geotechnical Engineering\Spring Coursework\TX4A200.xlsx")
ExForce = pd.DataFrame(data, columns= ['Force (N)'])
Force = ExForce.to_numpy(dtype='float', na_value=np.nan)  
ExStroke = pd.DataFrame(data, columns= ['Stroke (mm)'])
Stroke = ExStroke.to_numpy(dtype='float', na_value=np.nan)  

l0 = 75#mm
A0mm = 1104#mm^2
A0 = A0mm/1000**2 #m^2

Strain = (Stroke/l0) * 100 #%
A = A0/(1-(Strain/100)) #m^2
Stress = (Force/A) / 1000 #kNm^-2

#Force and Displacement

plt.figure(1)
plt.plot(Stroke,Force,'blue')

plt.title("Cell 4 : 200 kPa Cell Pressure")
plt.xlabel("Axial Displacement (mm)")
plt.ylabel("Axial load (N)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

interactive(True)
plt.show()

#Axial Strain and Deviatoric Stress

plt.figure(2)
plt.plot(Strain,Stress,'blue')

plt.title("Cell 4 : 200 kPa Cell Pressure")
plt.xlabel("Axial Strain (%)")
plt.ylabel("Deviatoric Stress (kPa)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.show()

interactive(False)
plt.show()

"""
250kPa
"""

data = pd.read_excel(r"C:\Users\hk3rr\Desktop\University stuff\Year 2\CIV2500 - Geotechnical Engineering\Spring Coursework\TX5A250.xlsx")
ExForce = pd.DataFrame(data, columns= ['Force (N)'])
Force = ExForce.to_numpy(dtype='float', na_value=np.nan)  
ExStroke = pd.DataFrame(data, columns= ['Stroke (mm)'])
Stroke = ExStroke.to_numpy(dtype='float', na_value=np.nan)  

l0 = 75#mm
A0mm = 1104#mm^2
A0 = A0mm/1000**2 #m^2

Strain = (Stroke/l0) * 100 #%
A = A0/(1-(Strain/100)) #m^2
Stress = (Force/A) / 1000 #kNm^-2

#Force and Displacement

plt.figure(1)
plt.plot(Stroke,Force,'blue')

plt.title("Cell 5 : 250 kPa Cell Pressure")
plt.xlabel("Axial Displacement (mm)")
plt.ylabel("Axial load (N)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

interactive(True)
plt.show()

#Axial Strain and Deviatoric Stress

plt.figure(2)
plt.plot(Strain,Stress,'blue')

plt.title("Cell 5 : 250 kPa Cell Pressure")
plt.xlabel("Axial Strain (%)")
plt.ylabel("Deviatoric Stress (kPa)")

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.show()

interactive(False)
plt.show()