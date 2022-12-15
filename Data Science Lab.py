#!/usr/bin/env python
# coding: utf-8

# # 1.Installation of Python framework and study of various IDEs

# 1. Spyder
# 2. jupyer
# 
# 3. Reptil

# In[13]:





# In[3]:


#!pip install openpyxl


# # 2.Write a python program to implement basic mathematical operations

# In[4]:


x = 11
y = 12
z = x+y


# In[5]:


z


# In[6]:


print("The sum of inputed numbers are: ",z)


# or

# In[8]:


x = int(input("Enter First No: "))
y = int(input("Enter Second No.: "))
z = x+y
q = x-y
r = x*y
d = y/x

print("The sum of numbers are: ",z)
print("The diffrence between numbers is:",q)
print("The product of Number is: ",r)
print("The divident between number is: ",d)


# # 3.Write a python program to display max and min numbers(Out of numbers)

# In[10]:


if(x>y):
    print(x,"X is greater")
    
    
elif(x==y):
    print(x,y,"The numbers are equal")
    
    
else:
    print(y,"Y is greater")


# In[15]:


lst = [x,y,z]

print(lst)


t= max(lst)

a = min(lst)


print("The Maximum no is:",t)
print("The Minimum no. is:",a)


# In[ ]:




