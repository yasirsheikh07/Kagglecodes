#!/usr/bin/env python
# coding: utf-8

# In[1]:


course = "AI & Data Science"


# In[2]:


print(len(course))


# In[3]:


print(course[0])


# In[4]:


print(course[-1])


# In[8]:


print(course[0:1])


# In[10]:


print(course[0:2])


# In[13]:


print(course[0:20])


# In[16]:


print(course[0:-1])


# In[18]:


print(course[0:-16])


# In[20]:


print(course[0:-17])


# In[23]:


print(course[0:-18])


# In[24]:


print(course[:])


# In[39]:


course2 = 'Full Stack "Development'


# In[51]:


print(course2)


# In[52]:


course3 = "Full Stack 'Development"


# In[53]:


print(course3)


# In[54]:


course4 = 'Full Stack \"Development'


# In[55]:


print(course4)


# In[56]:


course5 = "Full Stack \'Development"


# In[57]:


print(course5)


# In[58]:


first_name = "Yasir"


# In[59]:


last_name = "Sheikh"


# In[65]:


full_name = first_name + "_" + last_name


# In[66]:


print(full_name)


# In[71]:


full_name = f"{first_name} {last_name}"


# In[72]:


print(full_name)


# In[127]:


name1 = "Mohammad"
name2 = "Nomaan"
name3 = "Waseem"
name4 = "Akhtar"

fullname_nomaan = f"{name1} {name2} {name3} {name4}"

print(fullname_nomaan)


# In[142]:


agent = "Monu Sheikh"

print(agent.upper())
print(agent.lower())
print(agent.replace("Sheikh", "Siddique"))


# In[143]:


agent1 = "abdul siddique"

print(agent1.title())
print(agent1.find("sid"))
print(agent1.find("Sid"))
print(agent1.replace("d", "p"))
print(agent1.replace("siddique", "rehman"))


# In[144]:


agent2 = "      100              Rafe Ansari               1      "

print(agent2.strip())
print(agent2.rstrip())
print(agent2.lstrip())


# In[152]:


agent3 = "Asad Bhau"

print("Asad" in agent3)
print("Monu" in agent3)


# In[156]:


agent4 = "Zaki Akola"

print("Zaki" in agent4)
print("Monu" not in agent4)


# In[161]:


print(round(3.333))
print(round(3.9999))
print(abs(3.333))
print(abs(3.9999))


# In[185]:


print(math.ceil(3.01))
print(math.ceil(3.0000000001))
print(math.ceil(3.9))
print(math.ceil(3.0000000000000000000000000000000000000000000000000001))
print(math.ceil(3.0))
print(math.ceil(-1))
print(math.ceil(-3.1))
print(math.ceil(-4.9))


# In[191]:


10 % 6


# In[193]:


10 / 5


# In[194]:


10 % 10


# In[195]:


10 % 7


# In[196]:


11 % 1


# In[198]:


10 < 20


# In[199]:


20 > 10


# In[210]:


"bag" > "apple"


# In[213]:


"apple" > "bag"


# In[214]:


"Nomaan" > "Moin"


# In[1]:


ord("B")

