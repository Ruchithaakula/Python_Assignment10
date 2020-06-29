#!/usr/bin/env python
# coding: utf-8

# In[1]:


color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# In[ ]:




