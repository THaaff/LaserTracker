# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:35:41 2018

@author: ibaby  (Taylor)
"""

import math as m
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#pupil labs outputs
df = pd.read_csv('gaze_positions.csv')
df['pixel_x_mean'] = df['pixel_x'].groupby(df['index']).mean()
df['pixel_y_mean'] = df['pixel_y'].groupby(df['index']).mean()

x = df['pixel_x_mean'].dropna()
y = df['pixel_y_mean'].dropna()

#plt.scatter(x,y)
#plt.xlim(0,1280)
#plt.ylim(0,720)

#plt.scatter(df['pixel_x'],df['pixel_y'])
#plt.xlim(0,1280)
#plt.ylim(0,720)

df1 = pd.read_excel("C:\\Users\\ibaby.ADS\\Downloads\\ball-tracking\\laser_pupil.xlsx")
gx = df1['gx']
gy = df1['gy']

#plt.scatter(gx,gy, alpha = .25, color = 'g')
#plt.xlim(0,1280)
#plt.ylim(0,720)

rx = df1['rx']
ry = df1['ry']

#plt.scatter(rx,ry, alpha = .25, color = 'r')
#plt.xlim(0,1280)
#plt.ylim(0,720)

#moving pupil labs output to CV df
df1['pixel_x_mean'] = df['pixel_x_mean']
df1['pixel_y_mean'] = df['pixel_y_mean']

#df1['gp_xdiff'] = gx - df1['pixel_x_mean']
#df1['gp_ydiff'] = gy - df1['pixel_y_mean']

df1['gp_xdiff'] = gx - rx
df1['gp_ydiff'] = gy - ry

#plt.plot(df1['gp_xdiff'])
#plt.plot(df1['gp_ydiff'])
#plt.xlim(60,700)
#plt.ylim(-500,400)

#plt.scatter(df['gaze_normal1_x'],df['gaze_normal1_y'])
#plt.scatter(df['gaze_normal0_x'],df['gaze_normal0_y'], color = 'r')
plt.scatter(df['norm_pos_x'],-df['norm_pos_y'], color = 'g')

'''

'''