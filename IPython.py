#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#IPython


# In[ ]:


get_ipython().show_usage()

get_ipython().run_line_magic('pinfo2', '')

help()


# In[ ]:


help(len)


# In[ ]:


help(square)


# In[ ]:


get_ipython().run_line_magic('pinfo2', 'square')


# In[ ]:


conda install -c anaconda ipython


# In[7]:


conda install -c anaconda ipython


# In[8]:


help(len)


# In[9]:


def square(a):
    
    return a ** 2


# In[13]:


help(square)


# In[11]:


get_ipython().run_line_magic('pinfo', 'len')


# In[16]:


get_ipython().run_line_magic('pinfo2', 'square')


# In[ ]:


# help- keyboard shortcuts


# In[19]:


conda update -n base -c defaults conda


# In[20]:


conda install -c conda-forge python-magic


# In[21]:


#Magics need to know:

#%lsmagic
#%run
#%timeit

# Two types:

#Line magics are used with a % prefix and operate on one line only
#Cell magics are used with %% prefix and operate on multiple lines


# In[22]:


get_ipython().run_line_magic('lsmagic', '')


# In[23]:


get_ipython().system('pwd')


# In[24]:


get_ipython().run_cell_magic('writefile', 'hello.py', '\ndef main():\n    print("Hello")\n    \nmain()')


# In[25]:


get_ipython().run_line_magic('run', 'hello.py')


# In[26]:


#Input and Output History


# In[27]:


import math

print(math.sin(2))
print(math.cos(2))


# In[28]:


print(In)


# In[30]:


print(In[6])


# In[31]:


get_ipython().run_line_magic('history', '')


# In[32]:


print(Out[2])


# In[ ]:


#Underscore shortcuts and previous outputs 
# shortcut for accessing previous output is variable _, a single underscore
# it is updated with previous output 


# In[33]:


1+1


# In[34]:


_*2


# In[35]:


_*2


# In[37]:


print(_,__,___)


# In[ ]:


#Shell Commands in Ipython


# In[38]:


get_ipython().system('ls')


# In[39]:


get_ipython().system('pwd')


# In[41]:


get_ipython().run_line_magic('bash', '')
    get_ipython().system('ls')


# In[46]:


get_ipython().run_cell_magic('cmd', '', '')


# In[47]:


get_ipython().system('cd')


# In[48]:


get_ipython().system('pwd')


# In[49]:


get_ipython().run_line_magic('cd', '')


# In[50]:


get_ipython().run_line_magic('cd', 'Desktop')


# In[51]:


get_ipython().run_line_magic('mkdir', 'example')


# In[52]:


get_ipython().run_line_magic('cd', './example')


# In[ ]:




