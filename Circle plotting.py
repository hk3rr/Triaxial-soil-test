# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 17:15:03 2022

@author: hk3rr
"""

import matplotlib.pyplot as plt

circle1 = plt.Circle((279, 0), 229, color='r', fill = False, label = '50 kPa Cell Pressure')
circle2 = plt.Circle((378, 0), 278, color='g', fill = False, label = '100 kPa Cell Pressure')
circle3 = plt.Circle((528, 0), 278, color='b', fill = False, label = '250 kPa Cell Pressure')

fig, ax = plt.subplots() 

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

plt.axhline(y = 278, color = 'r', linestyle = '--')

plt.axhline(y = -278, color = 'r', linestyle = '--')

plt.xlim([0,1200])
plt.ylim([-500,500])

plt.minorticks_on()
plt.grid(visible = True, which = 'major')
plt.grid(visible = True, which = 'minor', linestyle='--')

plt.title("Total stresses at failure")
plt.xlabel("Normal Stress (kPa)")
plt.ylabel("Shear Stress (kPa)")

plt.legend(loc="upper right")