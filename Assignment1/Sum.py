#!/usr/bin/env python
# coding: utf-8

# In[11]:


num = int(input("Enter the number"))

if num<0:
    print("Please enter a positive number")
else:
    i = 0
    sum=0
    while i<=num:
        sum+=i
        i+=1
    print("Sum of ",num," number/s is ",sum)

    
    

