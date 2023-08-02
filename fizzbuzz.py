#!/usr/bin/env python
# coding: utf-8

# In[4]:


for i in range (1,101):
    if 1 == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
    elif i % 3 == 0:
        print("fizz")
        continue
    elif i % 5 == 0:
        print("buzz")
        continue
    print(i)


# In[ ]:




