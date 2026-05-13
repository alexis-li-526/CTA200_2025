#!/usr/bin/env python
# coding: utf-8

# In[1]:


def if_diverge(z):
    c = z[0] + z[1]*1j
    i = 0
    z_i = 0
    # checks for divergence
    while i < 1000:
        i += 1
        z_f = z_i**2 + c
        if abs(z_f) > 2:
            return i
        z_i = z_f
    return False


# In[ ]:




