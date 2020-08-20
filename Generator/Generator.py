
# coding: utf-8

# In[5]:


#Genarator function
def func(a):
    yield a #change keyword return to yield
a = [1,2,3]
b=func(a)
next(b)


# In[11]:


#Normal function
def func(a):
    return a

a = [1,2,3]
func(a)


# In[15]:


def gen_func(a):
    while a >= 3:
        yield a
        a+=1
b = gen_func(5)
print(b)
next(b)


# In[17]:


next(b)


# In[18]:


a = 2
def gen_fn(a):
    while a >= 0:
        yield a
        a -=1
b = gen_fn(a)
print(b)
next(b)


# In[19]:


next(b)


# In[20]:


next(b)


# In[21]:


next(b)


# In[24]:


def z():
    n =1 
    yield n
    n = n+3
    yield n
p = z()
next(p)


# In[25]:



next(p)


# In[26]:



next(p)


# In[27]:


def z():
    n =1 
    yield n
    n = n+3
    yield n
    
    n = n+4
    yield n
p = z()
next(p)


# In[28]:


next(p)


# In[29]:


next(p)


# In[30]:


next(p)


# In[34]:


def send_me_list(list):
    for i in range(len(list)):
        yield list[i]


# In[35]:


object_of_gen= send_me_list([2,3,4,5,56,6,7,6,54])
next(object_of_gen)


# In[37]:


next(object_of_gen)


# In[38]:


next(object_of_gen)

