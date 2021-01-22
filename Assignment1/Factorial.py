#!/usr/bin/env python
# coding: utf-8

# In[3]:


num = int(input("Enter the number"))

if num<0:
    print("Factorial of a negative number doesn't exists")
elif num==0 or num==1:
    print("Factorial of ",num," is ",1)
else:
    fact = 1
    for each in range(2,num+1):
        fact *= each
    print("Factorial of ",num," is ",fact)
    
    
                
    
    

