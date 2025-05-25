#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=1
if x==2:
    print("No. is 2")
else:
    print("No. is not 2")
    


# In[6]:


float1=2.1
float2=3.5
print(float1 + float2)


# In[7]:


n = int(input("Enter no: "))
if n % 2 == 0 and 2<=n<=5 :
    print("Not weird")
elif n % 2 == 0 and 6<=n<=20:
    print("Weird")
elif n % 2 == 0 and n>20:
    print("Not weird")
elif n % 2 != 1:
    print("Weird")


# In[ ]:





# In[8]:


a = int(input("Enter first no "))
b = int(input("Enter second no "))

if a*b > 1000:
    print("Sum is: " + str(a+b))
else:
    print("Product is:" + str(a*b))


# In[ ]:





# In[10]:


a = "Hello"
print(a[0:1])


# In[12]:


def asc_des_none(lst, s):
    if s == "Asc":
        return lst.sort()
    elif s == "None":
        return lst
    elif s == "Des":
        return lst.sort(reverse = True)

asc_des_none([1,2,3,4], "None")


# In[ ]:





# In[ ]:





# In[13]:


#2 (YT)
a= 5
b= 6
a,b= b,a
print (a,b)


# In[14]:


#3 Changing Data Type
a= 5.6
a= int(a)
print (a)


# In[17]:


#5
a = int(input("Enter integer no: "))
a = float(a)
print("It's float is:", a)


# In[37]:


a = int(input("Enter an integer:"))
if a > 0:
    print("No. is positive")
elif a == 0:
    print("No. is zero")
elif a < 0:
    print("No. is negative")
else:
    print("Invalid Input")


# In[39]:


a = int(input("Enter an integer:"))
if a%2 == 0:
    print("Even")
else:
    print("Odd")


# In[70]:


#Checking Vowel or Consonent
a = input("Enter any alphabet: ")
print(a)
if a in ('a','e','i','o','u') or a in ('A','E','I','O','U'):
    print("Vowel")
else:
    print("Consonant")


# In[73]:


a = int(input("Enter a no upto 3 digits: "))
print(a)
if a >= 0 and a < 9:
    print("Single digit")
elif a >= 10 and a < 99:
    print("Double digit")
elif a >= 100 and a < 999:
    print("Triple digit")
else:
    print("Invalid no.")


# In[80]:


#printing odd digits in given range
for i in range (1,7,2):
    print (i)


# In[82]:


#printing table
n = 5
for i in range (1,11):
    print(n,"*",i,"=",n*i)


# In[83]:


for i in range(1,5):
    for j in range (1,11):
        print (j, end = "")
    print()


# In[84]:


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




