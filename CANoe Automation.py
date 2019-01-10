
# coding: utf-8

# In[2]:


import pyautogui


# In[3]:


# To pause:
pyautogui.PAUSE = 1


# In[5]:


pyautogui.FAILSAFE = False


# In[8]:


# get screen size:
pyautogui.size()
width, height = pyautogui.size()
#to move with duration fixed: use this to wait for canoe.exe to start:
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
    break


# In[10]:


# getting current position:
pyautogui.position()


# In[11]:


# Click:
pyautogui.click(10, 5)
#double click:
pyautogui.doubleClick()
#right click:
pyautogui.rightClick()
#middle click:
pyautogui.middleClick()


# In[12]:


# mouse up and down . use to DRAG:
pyautogui.mouseDown()
pyautogui.mouseUp()


# In[13]:


#scroll:
pyautogui.scroll(200)


# In[20]:


#use this to match the start button in canoe and then click. Include wait() before this step.
im = pyautogui.screenshot()
im.getpixel((0, 0))
rgb= im.getpixel((50, 200))
pyautogui.pixelMatchesColor(50, 200, (rgb))


# In[21]:


rgb= im.getpixel((50, 200))
rgb


# In[ ]:


# use png of the start button to click it once it appears:
pyautogui.locateOnScreen('Untitled.png')


# In[38]:


#then get the center of the image on scrren . use this coordinate to click:
pyautogui.center((391, 74, 111, 35))


# In[47]:


import time
time.sleep(5)
pyautogui.click(446, 91)

