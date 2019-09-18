#!/usr/bin/env python
# coding: utf-8

# Initialize. Call the commandoes:

# In[1]:


# Initialization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import quad
import math
from math import exp, expm1


# Class definition.
# The class is defined with the following variables:
# 
# Stream is the number or name of the stream
# 
# Flow is the flow for the specific stream [=] m3/h
# 
# Concentration is the concentration for the specific component [=] mol/m3
# 
# The class is now defined:

# In[2]:


class BatchReactor:
    def __init__(self, Stream, Flow, Concentration):
        self.Stream = Stream
        self.Flow = Flow
        self.Concentration = Concentration

#For this example the calculations are done with 1 streams obtaining the following name and value:
#For stream number 1 the flow is 100 m3/h and the concentration is 2 mol/m3
batchreactorA = BatchReactor("Stream A", 100, 2)


# In[3]:


# The reaction is: A_in -> B + A_out
#Where A_in is the parameters in the class


# In[4]:


# Constants definitions
#The time for the inflow is now defined. This specifies for how long the streams will go into the mixer.
#The unit is in hours. For this example the simulation will run for 10 h
T_inflow = 10

#Reactor conversion [0;1]
X_reaction = 0.9

# Reaction rate constant, k:
k_reaction = 1.5


# In[5]:


# Variable definition
#The time is now made as an interval going from 1 to the T_inflow value 
time = np.arange(1,T_inflow)


# In[6]:


# Volume calculations 
# The volume going into the batch reactor is V = flow*t 
V_in = batchreactorA.Flow*time
#The constant volume after loading time is
V_reactor = batchreactorA.Flow*T_inflow


# In[7]:


#The concentrations of A_out and B are now calculated after the reaction

B_concentration = batchreactorA.Concentration*X_reaction

A_out_concentration = batchreactorA.Concentration*(1-X_reaction)

# The values of the concentrations are:
print('The value of CA_out is ' + repr(A_out_concentration) + ', and C_B is ' + repr(B_concentration))


# In[8]:


#The mixing time for the reaction is now calculated for a first order reaction 

def integrand(X_reaction):
    return batchreactorA.Concentration/(k_reaction*(1-X_reaction)*batchreactorA.Concentration)

t_reac, err = quad(integrand, 0, X_reaction)
print(t_reac)


# In[23]:


# Reaction time as an array
t_reaction = np.arange(0.001, t_reac, 0.01)


# In[27]:


#For en reaktion af første orden aftager koncentrationen af reaktanten A eksponentielt med tiden 
C_aftager = batchreactorA.Concentration*np.exp(-k_reaction*t_reaction)



# In[28]:


fig = plt.figure()
ax = plt.subplot(111)
ax.plot(t_reaction,C_aftager, label = 'Volume flow 1')
plt.title('Volume plot')
ax.legend()
plt.show()


# In[24]:


t_reaction


# In[15]:


C_aftager


# In[26]:


batchreactorA.Concentration*math.exp(-k_reaction)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




