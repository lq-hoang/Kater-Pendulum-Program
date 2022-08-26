# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 00:18:12 2022

Simple program taking in data collected at McLennan Physical Laboratories
of a Kater pendulum and creating linear models to graph. Program
also prints out the calculated values for each model to create two line
equations that can be used to find the accelaration due to gravity at 
the lab location.

@author: linh
"""
import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def linear_model(x, m, b):
    return ((m*x) + b)
'''
 adj_pos represents the position of the small weight on the pendulum.
 upright_time represents the recorded amount of time the pendulum takes 
 swinging while invert_time represents the recorded amount of time the 
 pendulum flipped upside down swings.
 u_uncertainty and i_uncertainty represents the measurement error found 
 for upright_time and invert_time respectively.
'''
adj_pos, upright_time, u_uncertainty, invert_time, \
    i_uncertainty = np.loadtxt("real_data.txt", skiprows = 8, 
                                          dtype = "float", delimiter=',', 
                                          unpack = True)

invert_time = invert_time / 8 # calculate to time for 1 period
upright_time = upright_time / 8 # calculate to time for 1 period
i_uncertainty = i_uncertainty / 8 # calculate to uncertainty for 1 period
u_uncertainty = u_uncertainty / 8 # calculate to uncertainty for 1 period

popt_i, pcov_i = curve_fit(linear_model, adj_pos, invert_time, 
                           sigma = i_uncertainty, absolute_sigma = True)
m_i = popt_i[0]
b_i = popt_i[1]
pstd_i = np.sqrt(np.diag(pcov_i))
print("Inverted m =", m_i, "+-", pstd_i[0])
print("Inverted b =", b_i, "+-", pstd_i[1])

popt_u, pcov_u = curve_fit(linear_model, adj_pos, upright_time, 
                           sigma = u_uncertainty, absolute_sigma = True)
m_u = popt_u[0]
b_u = popt_u[1]
pstd_u = np.sqrt(np.diag(pcov_u))
print("Upright m =", m_u, "+-", pstd_u[0])
print("Upright b =", b_u, "+-", pstd_u[1])


model_i = linear_model(adj_pos, m_i, b_i)
model_u = linear_model(adj_pos, m_u, b_u)
plt.plot(adj_pos, model_i, "g", label = "Model inverted pendulum")
plt.plot(adj_pos, model_u, "black", label = "Model upright pendulum")

plt.scatter(adj_pos, invert_time, color = "r", label = "Experiment inverted Pendulum")
plt.errorbar(adj_pos, invert_time, yerr = i_uncertainty, linestyle = '',
             color = "r")

plt.scatter(adj_pos, upright_time, label = "Experiment upright Pendulum")
plt.errorbar(adj_pos, upright_time, yerr = u_uncertainty, linestyle = '')
plt.xlabel("Position of fine adjustment weight")
plt.ylabel("Period (s)")
plt.legend()
plt.title("Period for 2 pendulums (s) vs Position of fine adjustment (cm)")

# goodness of fit
summation_u = 0
summation_i = 0
for i in range(len(upright_time)):
    summation_u += ((upright_time[i] - model_u[i])/u_uncertainty[i])**2
    summation_i += ((invert_time[i] - model_i[i])/i_uncertainty[i])**2
    
chi_i = (1/4)*(summation_i)
chi_u = (1/4)*(summation_u)
print("Reduced-Chi Squared value for inverted pendulum is: ", chi_i)
print("Reduced-Chi Squared value for upright pendulum is: ", chi_u)

plt.show()
