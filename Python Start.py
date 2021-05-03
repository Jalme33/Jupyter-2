#!/usr/bin/env python
# coding: utf-8

# In[20]:


number = 23

while chances < 5 :

guess = int(input('Enter an integer from 1 to 50: '))

if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win any prizes!)')
    
elif guess < number:
     print('No, it is a little higher than that')
elif guess > number: 
     print('No, a bit lower')


# In[ ]:





# In[ ]:





# In[16]:


9


# In[18]:


vowels = "AEIOU"
for iter in vowels:
    print("char:", iter)


# In[19]:


for x in range(10):
    print (x+1)


# In[ ]:


number = 23

chances = 0

while chances < 5 :
    
    guess = int(input('Enter an integer from 1 to 50: '))

if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win anything lol!)')
    
elif guess < number:
     print('No, it is a little higher than that')
elif guess > number: 
     print('No, a bit lower')
else print ('done')


# In[ ]:


number = 23

chances = 0

while chances < 5 :
    
    guess = int(input('Enter an integer from 1 to 50: '))

if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win anything lol!)')
    
elif guess < number:
     print('No, it is a little higher than that')
elif guess > number: 
     print('No, a bit lower')
    chances += 1
else:
    print ('done')


# In[ ]:


def while_else_demo():
    count = 0
    while count < 5 :
        num = int(input("Enter number between 0-100?"))
        if (num < 0) or (num > 100):
            print("Aborted while: You've entered an invalid number.")
            break
        count += 1
    else:
        print("While loop ended gracefully.")


# In[ ]:





# In[ ]:


number = 23

chances = 0

while (chances < 5 :and guess != number):
    
    guess = int(input('Enter an integer from 1 to 50: '))

if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win anything lol!)')
    
elif guess < number:
     print('No, it is a little higher than that')
elif guess > number: 
     print('No, a bit lower')
    chances += 1
else:
    print ('done. chances:')
    print(chances)


# In[ ]:


number = 23

chances = 0

while (chances < 5 :and guess != number):
    
    guess = int(input('Enter an integer from 1 to 50: '))

if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win anything lol!)')
    
elif guess < number:
     print('No, it is a little higher than that')
elif guess > number: 
     print('No, a bit lower')
    chances += 1
else:
    print ('done. chances:')
    print(chances)


# In[1]:


23


# In[ ]:


def dogyears():
    age = float(input("What is your age? "))
    # dog years = human years * 7
    dy = age * 7
    print("Your age is", dy, "dog years")


# In[ ]:


dogyears()


# In[ ]:


def exponent():
    for i in range(10)
        print(i**(i+1))


# In[ ]:


exponent()


# In[2]:


anaconda upload Python Start.ipynb


# In[ ]:




