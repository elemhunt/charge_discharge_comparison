# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------#
# Time Correction Vales
# Note: The First data point is always 'nan' so the correction value
#       must be input manually.
#------------------------------------------------------------------------#
correction_val1 = 1921.07805314974
correction_val2 = 2916.68356563608
correction_val3 = 3049.02881130194
correction_val4 = 3071.83306624437
correction_val5 = 3076.9699652314

#------------------------------------------------------------------------#
# Load in Data
# Note: route of .txt files may need to be changes depending on directory
#------------------------------------------------------------------------#

data_file_1 = np.genfromtxt('/Users/elemhunt/Desktop/Plot/S035/_CD_20e-6A_3C.txt')
data_file_2 = np.genfromtxt('/Users/elemhunt/Desktop/Plot/S035/_CD_50e-6A_3C.txt')
data_file_3 = np.genfromtxt('/Users/elemhunt/Desktop/Plot/S035/_CD_100e-6A_3C.txt')
data_file_4 = np.genfromtxt('/Users/elemhunt/Desktop/Plot/S035/_CD_200e-6A_3C.txt')
data_file_5 = np.genfromtxt('/Users/elemhunt/Desktop/Plot/S035/_CD_500e-6A_3C.txt')

#------------------------------------------------------------------------#
# Set Columns and Data Points
#------------------------------------------------------------------------#
time1 = data_file_1[1:,0]
fix_time1 = time1 - correction_val1
voltage1 = data_file_1[1:,2]

time2 = data_file_2[1:,0]
fix_time2 = time2 - correction_val2
voltage2 = data_file_2[1:,2]

time3 = data_file_3[1:,0]
fix_time3 = time3 - correction_val3
voltage3 = data_file_3[1:,2]

time4 = data_file_4[1:,0]
fix_time4 = time4 - correction_val4
voltage4 = data_file_4[1:,2]

time5 = data_file_5[1:,0]
fix_time5 = time5 - correction_val5
voltage5 = data_file_5[1:,2]


#------------------------------------------------------------------------#
# Plots
# Note: Legend and line color/width may need to be changed accrodingly
#------------------------------------------------------------------------#


fig, ax = plt.subplots()
l1 = ax.plot(fix_time1,voltage1,'r', linewidth=2.0)
l2 = ax.plot(fix_time2,voltage2,color='orange', linewidth=2.0)
l3 = ax.plot(fix_time3,voltage3,'g', linewidth=2.0)
l4 = ax.plot(fix_time4,voltage4,'b', linewidth=2.0)
l5 = ax.plot(fix_time5,voltage5,'m', linewidth=2.0)

ax.legend(['20e-6 A','50e-6 A','100e-6 A','200e-6 A', '500e-6 A'],loc='best')
ax.set_title('CD Comparison')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')

fig.savefig('CD Comparison', dpi = 1000)

fig, ax1 = plt.subplots()
ax1.plot(fix_time1,voltage1,'r', linewidth=2.0)
ax1.legend(['20e-6 A'],loc='best')
ax1.set_title('CD Comparison')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)')

fig.savefig('CD - 20e-6A', dpi = 1000)


fig, ax2 = plt.subplots()
ax2.plot(fix_time2,voltage2,'orange', linewidth=2.0)
ax2.legend(['50e-6 A'],loc='best')
ax2.set_title('CD Comparison')
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Voltage (V)')

fig.savefig('CD - 50e-6A', dpi = 1000)

fig, ax3 = plt.subplots()
ax3.plot(fix_time3,voltage3,'g', linewidth=2.0)
ax3.legend(['100e-6 A'],loc='best')
ax3.set_title('CD Comparison')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Voltage (V)')

fig.savefig('CD - 100e-6A', dpi = 1000)

fig, ax4 = plt.subplots()
ax4.plot(fix_time4,voltage4,'b', linewidth=2.0)
ax4.legend(['200e-6 A'],loc='best')
ax4.set_title('CD Comparison')
ax4.set_xlabel('Time (s)')
ax4.set_ylabel('Voltage (V)')

fig.savefig('CD - 200e-6A', dpi = 1000)

fig, ax5 = plt.subplots()
ax5.plot(fix_time5,voltage5,'m', linewidth=2.0)
ax5.legend(['500e-6 A'],loc='best')
ax5.set_title('CD Comparison')
ax5.set_xlabel('Time (s)')
ax5.set_ylabel('Voltage (V)')

fig.savefig('CD - 500e-6A', dpi = 1000)