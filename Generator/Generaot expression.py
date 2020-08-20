
# coding: utf-8

# ## Generator Expression : 

# In[1]:


a = range(6)
print("list of Comprehension ", end=':')


# In[2]:


a=range(6)
print("List Comprehension", end=':')


# In[6]:


b = [number for number in a]
print(b)


# In[7]:


print("Generator expression " , end = ':n')


# In[12]:


c= (x for x in a)
#next(c)
#next(c)
for y in c:
    print(y)


# ## Use Cases :

# In[14]:


def fibo():
    first , seconed = 0 ,1
    while True:
        yield first
        first , seconed = seconed , first+seconed
for x in fibo():
    if x>50:
        break
    print(x ,end =  " ")


# ## Generating Numbers:

# In[24]:


a = range(1,10,2) #change parameter to take odd and even value
x = (x for x in a)
print(b)
for y in b:
    print(y)

