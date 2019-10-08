#!/usr/bin/env python
# coding: utf-8

# Initialize. Call the commandoes:

# In[1]:


# Initialization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataclasses as dataclass
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math


# In[2]:


# Making the class of the mixer
class BatchMixer:
    def __init__(self, Component, Stream, X_component, mass_stream, mass_component):
        self.Component = Component
        self.Stream = Stream 
        self.X_component = X_component
        self.mass_stream = mass_stream
        self.mass_component = mass_component
        
# Expample values:
batch = [BatchMixer("Sugar",  1, 2.5 , 125 , 'X'), 
         BatchMixer("Water",  1, 50  , 125 , 'X'),
         BatchMixer("Solids", 1, 47.5, 125 , 'X'),
         BatchMixer("Sugar",  2, 1   , 45  , 'X'),
         BatchMixer("Water",  2, 18  , 45  , 'X'),
         BatchMixer("Solids", 2, 31  , 45  , 'X'),
         BatchMixer("Sucrose",2, 50  , 45  , 'X'),
         BatchMixer("Water",  3, 100 , 8.75, 'X')]


# In[10]:


# Mass calculations 
Mass_component = []
Component_array = []
for b in batch:
    b.mass_component = (b.X_component/100)*b.mass_stream
    Mass_component.append(b.mass_component)
    Component_array.append(b.Component)
Mass_total = sum(Mass_component) 

print('The total mass is ' + repr(Mass_total) + ' kg')


# In[6]:


#Removing duplicates:
components = list(dict.fromkeys(Component_array))

# Total mass of each component
for m in range(len(components)):
    mass = [];
    conc = [];
    for b in batch:
        if components[m] == b.Component:
            mass.append(b.mass_component)
            conc.append(b.mass_component/Mass_total*100)
    print('The total mass of ' + repr(components[m]) + ', is ' + repr(sum(mass)) + ' kg');
    print('The total concentration of ' + repr(components[m]) + ', is ' + repr(sum(conc)) + ' %');


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




