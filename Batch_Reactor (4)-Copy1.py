#!/usr/bin/env python
# coding: utf-8

# Initialize. Call the commandoes:

# In[1]:


# Initialization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import quad
from scipy.integrate import odeint
import math
from math import exp, expm1
from dataclasses import dataclass


# In[2]:


#Defining the classes:
class BatchReactant:
    def __init__(self, Name, Number, Coefficient, Concentration, Order, EndConcentration):
        self.Name = Name # The reactant is given a name 
        self.Number = Number # The reactant is given a number
        self.Coefficient = Coefficient # The reactant coefficient  
        self.Concentration = Concentration # The reactant concentration
        self.Order = Order # The reactant order
        self.EndConcentration = EndConcentration # The unknown end concentration. 

reactant = [BatchReactant("Component A", 1, 1, 1, 2, 'X')]

class BatchProduct:
    def __init__(self, Name, Coefficient, Concentration, EndConcentration):
        self.Name = Name #The product is given a name
        self.Coefficient = Coefficient
        self.Concentration = Concentration
        self.EndConcentration = EndConcentration

product = [BatchProduct("Product B", 1, 0, 'X')]


class BatchReaction:
    def __init__(self, Reaction, Conversion, Rate, Volume):
        self.Reaction = Reaction
        self.Conversion = Conversion
        self.Rate = Rate
        self.Volume = Volume
        
reaction = BatchReaction("Reaction 1", 0.9, 10**(-3), 10)

# The reaction is given a name
# The conversion is entered as Convension 
# The rate is entered as Rate
# The volume of the batch is constant and entered as Volume


# In[3]:


# Finding the limiting reactant amount
Amount = [];
for r in reactant:
    amount = r.Concentration/r.Coefficient
    Amount.append(amount)
    Limit_amount = min(Amount)
    if Limit_amount == amount:
        limit_coef = r.Coefficient 
        limit_concentration = r.Concentration
        limit_number = r.Number


# In[4]:


# End concentration reactant
for r in reactant:
    r.EndConcentration = r.Concentration-r.Coefficient/limit_coef*limit_concentration*reaction.Conversion 


# In[5]:


# End concentration products
for p in product:
    p.EndConcentration = p.Concentration+p.Coefficient/limit_coef*limit_concentration*reaction.Conversion


# In[6]:


# Printing the end concentrations:
for r in reactant:
    print('The final concentration of ' + str(r.Name) + ', is ' + str(r.EndConcentration))
for p in product:
    print('The final concentration of ' + str(p.Name) + ', is ' + str(p.EndConcentration))


# In[7]:


#The mixing time for the reaction is now calculated:
def integrand(X):
    rate=1;
    for r in reactant:
        Q = (r.Concentration-r.Coefficient/limit_coef*limit_concentration*X)**(r.Order)
        rate = rate*Q
    return limit_concentration/(reaction.Rate*rate)
t_react, err = quad(integrand, 0, reaction.Conversion)
print(t_react/(60*60))


# In[8]:


#The time is made into a vector
time = np.linspace(0,t_react,num=100)


# In[9]:


# The reaction kinetics for the reactants 
Concentration_reactant_initial = [];
Order_reactant = [];
for r in reactant:
    Concentration_reactant_initial.append(r.Concentration)
    Order_reactant.append(r.Order)


# In[10]:


# Model the system for the reactants
def model_reactant(Conc_r, time):
    rate_r = 1;
    for c in range(len(Concentration_reactant_initial)):
        each_r = Conc_r[c-1]**Order_reactant[c-1]
        rate_r = rate_r * each_r
    dCrdt = [];
    for r in reactant:
        dCrdt.append(-reaction.Rate*rate_r*r.Coefficient/limit_coef)
    return dCrdt


# In[11]:


#Solve the reactant system
sol_r = odeint(model_reactant, Concentration_reactant_initial, time)


# In[12]:


# Plot the reactants 
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,sol_r[:,0], label = 'Ca')
plt.title('Concentration profile of reactants')
ax.legend()
plt.show()


# In[13]:


# Finding the limiting solution vector:
reactant_limiting_solution = sol_r[:,(limit_number-1)]


# In[14]:


# Model the system for the products 
dCpdt = [];
for p in product:
    dCpdt.append(p.Concentration+p.Coefficient/limit_coef*(limit_concentration - reactant_limiting_solution))


# In[15]:


# Plot the products
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,dCpdt[0], label = 'CB')
plt.title('Concentration profile of products')
ax.legend()
plt.show()


# In[16]:


#Plot of the products and reactants:
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(time,sol_r[:,0], label = 'Ca')
ax.plot(time,dCpdt[0], label = 'Cd')
plt.title('Concentration profile of reactants and products')
ax.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




