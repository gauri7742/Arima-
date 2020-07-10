import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

day=100  #number of days
dt=1  #step in number of days
beta=(1.0/3.0 ) #infection rate
gamma=(1.0/14.0) #recovery rate
s=np.zeros(day)  #susceptible
I=np.zeros(day)  #Infected
R=np.zeros(day)  #recoverd
t=np.arange(day)*dt

I[0]=0.001  #iniial infective proportion
s[0]=1-I[0] #iniial susceptible proportion
R[0]=0





for i in range (day-1):
  s[i+1]= s[i] -  beta*(s[i]*I[i])*dt
  I[i+1]=I[i] +  (beta*s[i]*I[i]-gamma*I[i])*dt
  R[i+1]=R[i] +  (gamma*I[i])*dt




  fig=plt.figure(1);
  fig.clf()
  plt.plot(t,s,'r',lw=3,label='Susceptible')
  plt.plot(t,I,'g',lw=3,label='Infection')
  plt.plot(t,R,'b',lw=3,label='recovered')
  fig.legend();
  plt.xlabel('DAYS')
  plt.ylabel('Fraction of Population')