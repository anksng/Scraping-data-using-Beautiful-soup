
# coding: utf-8

# In[202]:


import urllib.request
from bs4 import BeautifulSoup
import requests
import numpy as np


# In[64]:


page_url = 'https://en.wikipedia.org/wiki/Hildesheim'
# imdb_url = 'https://www.imdb.com/search/title?genres=drama&groups=top_250&sort=user_rating,desc'    


# **Urllib returns HTML to the assigned variable**

# In[65]:


html = urllib.request.urlopen(page_url).read()
html


# In[16]:


# page_imdb = urllib.request.urlopen(imdb_url)


# **page and page_imdb contains HTML. Next > Parse the html** <br>
# **Using Beautiful soup to parse**

# In[67]:


soup = BeautifulSoup(html, 'html.parser')   # Parser- html, lxml etc.
#parsed!
soup   # beautiful soup object


# In[20]:


# soup1 = BeautifulSoup(page_imdb, 'html.parser')


# # title()

# In[68]:


print('To get the title with tags:',soup.title)
print('To get the name of the tag:',soup.title.name)
print('To get the data within the <title> tag:',soup.title.string)
print(soup.title.text)   ## whats the difference with .string! ?


# # find, findAll('tag')

# In[70]:


print(soup.find('p'))
print(soup.p.text)


# In[71]:


for i in soup.findAll('p'):

    print(i.text)


# In[75]:


for i in soup.findAll('h2'):
    print(i.text)


# # to get all text()

# In[88]:


soup.getText(strip=True)


# # Get all links from the page:

# In[ ]:


# this gives all the links with tags: 
for i in soup.findAll('a'):
    print(i)     # i.text here will give all text whih is linked with another link. To get the link use .get


# In[99]:


#To get the link use .get
for i in soup.findAll('a'):
    print(i.get('href'))


# In[128]:


table = soup.findAll('table',attrs={'class':'wikitable'})
for i in table:
    print(i.text)


# In[139]:


table = soup.findAll('ul')
for i in table:
    print(i.text)


# # Scraping tables:
# '< tr >' table rows   <br>
# '< td >' table data<br>
# '< th >' table heading<br>

# In[170]:


table = soup.table
print(table.text)


# In[169]:


# table = soup.findAll('table',attrs={'class':'wikitable'})
# reading table rows:
# table_rows = table.findAll('tr')
# print(table_rows)
# table.findAll('tr')


# In[182]:


for i in table.findAll('tr'):
    table_data = i.findAll('td')
    row_data = [x.text for x in table_data]
    print(row_data)


# ### Using pandas to scrape tables from HTML :

# In[172]:


import pandas as pd


# In[180]:


df = pd.read_html(page_url,header=0)


# In[181]:


for i in df:
    print(i.head())


# # Lets pull out imdb top 250 movieslist and save it as a Dictionary :

# In[208]:


from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])
  


# In[214]:


imdb[0]

