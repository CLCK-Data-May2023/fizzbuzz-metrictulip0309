#!/usr/bin/env python
# coding: utf-8

# In[5]:


for i in range (1,101):
    if 1 == 0:
        continue
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    print(i)


# In[ ]:




