#!/usr/bin/env python
# coding: utf-8

# # Data Preprocessing

# In[51]:


import numpy as np
# Given data matrix, (-1,-1) represents blockage , (100,100) represents Goal State
A= np.array([
    [(0.2,0.9),(0.8,1),(0.05,0.05),(0.8,0.9),(0.8,0.9),(-1,-1),(100,100),(0.05,0.05),(0.2,0.1),(-1,-1)],
    [(-1,-1),(0.05,0.05),(0.05,0.05),(-1,-1),(0.8,0.9),(0.8,0.9),(0.05,0.05),(0.05,0.05),(0.2,0.1),(0.2,0.1)],
    [(0.2,0.9),(-1,-1),(0.2,0.1),(-1,-1),(0.2,0.1),(-1,-1),(-1,-1),(-1,-1),(0.2,0.1),(0.2,0.1)],
    [(0.2,0.9),(-1,-1),(0.2,0.1),(-1,-1),(0.2,0.1),(0.3,0.9),(0.2,0.1),(0.2,0.1),(0.2,0.1),(0.2,0.1)],
    [(0.2,0.9),(-1,-1),(0.2,0.1),(-1,-1),(0.3,0.9),(0.2,0.1),(0.2,0.1),(0.2,0.9),(0.2,0.9),(0.2,0.1)],
    [(0.2,0.9),(0.2,1),(0.2,0.1),(0.3,0.9),(0.3,0.9),(0.2,0.1),(-1,-1),(-1,-1),(-1,-1),(0.05,0.05)],
    [(0.2,0),(0.2,0.1),(0.2,0.1),(0.05,0.05),(0.05,0.05),(0.05,0.05),(-1,-1),(0.05,0.05),(0.05,0.05),(0.05,0.05)],
    [(0,0),(0,0),(0,0),(0.05,0.05),(0.05,0.05),(0.05,0.05),(-1,-1),(0.05,0.05),(0.05,0.05),(0.05,0.05)],
    [(0,0),(0,0),(0,0),(0.05,0.05),(0.05,0.05),(-1,-1),(0.05,0.05),(0.05,0.05),(-1,-1),(0.05,0.05)],
    [(0,0),(0,0),(0,0),(-1,-1),(-1,-1),(-1,-1),(0.05,0.05),(0.05,0.05),(-1,-1),(-1,-1)]
    ])


# In[50]:


#Calculate [(1+PoD)(1+PoM)] for each cell with value PoD/PoM, whereas -1 represents blockage and Goal represent Goat state
final=[]
for i in A:
    inter=[]
    for j in i:
        if j[0]==100:
            inter.append('Goal')
        elif j[0]!=-1:
            inter.append((j[0]+1)*(j[1]+1))
        else:
            inter.append(-1)
    final.append(inter)

print('The Matrix is: \n',final)


# # Random Restart Hill Climbing algorithm

# In[52]:


def RandomRestartHCA(final, src, dest):
    pass


# In[53]:


RandomRestartHCA(final, src, dest)


# In[ ]:



