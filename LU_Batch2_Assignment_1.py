#!/usr/bin/env python
# coding: utf-8

# In[22]:


first = int(input("Enter the first number"))
last = int(input("Enter the last number"))
for each in range(first,last):
    if each > 1:
        #print("each is ",each)
        for i in range(2, each):
            if each%i == 0:
                break
        else:
            print(each,end=',')
                
    
    


# In[ ]:





# In[ ]:




