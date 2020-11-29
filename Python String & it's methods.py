#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Capitalize Method of String, it will convert 1st char in upper case & rest will be in small.


# In[1]:


str_Dummy = "my name is Ashish Singh"


# In[2]:


str_Dummy.capitalize()


# In[ ]:


#center method of string fill the padded string with char within specified string width


# In[3]:


d ='ashish'


# In[8]:


d.center(10,'*')


# In[ ]:


#Casefold method of string aggresivelly convert the string into small


# In[9]:


d= "Python IS AWESOME"


# In[10]:


d.casefold()


# In[ ]:


#Count method of string return the count of subtring from given string range


# In[12]:


d.count('IS',0,len(d))


# In[ ]:


#endswith method of string return 


# In[14]:


d.endswith('ME1')


# In[ ]:


#formatting


# In[15]:


print('my name is {}. my is age is {}'.format('Ashish',31))


# In[16]:


'Ashish123'.isalnum()


# In[17]:


'Ashish123'.isalpha()


# In[21]:


t=('1','2','3','4','5','5')


# In[22]:


print('*'.join(t))


# In[23]:


t={'mat': 1, 'that': 2}


# In[24]:


print('->'.join(t))


# In[25]:


def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


# In[32]:


num=4
print("The Factorial of " , num , "is ", factorial(num))


# In[39]:


d=lambda x:x*2


# In[41]:


print(d([1,2,3]))


# In[42]:


#find out odd numbers from given list
lst=[1,2,3,4,5,6,7,8,9,10,11]


# In[48]:


def toCheckOddEven(lst,funcType):
    if funcType == 'Even':
        new_list = list(filter(lambda x : (x%2==0),lst))
        return print(new_list)
    elif funcType == 'Odd':
        new_list = list(filter(lambda x : (x%2!=0),lst))
        return print(new_list)
    else:
        print("Provide valid function type Odd or Even")


# In[50]:


toCheckOddEven(lst,'Even ')


# In[ ]:


#Global variable


# In[53]:


c=10


# In[55]:


def add(x):
    c= x+10+c
    print(c)


# In[57]:


def test(x):
    global c
    c +=x
    print('Inside variable ',c)


# In[58]:


test(5)
print('Outside variable ',c)

