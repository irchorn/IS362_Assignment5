#!/usr/bin/env python
# coding: utf-8

# # IS362 Assignment 5

# In[1]:


import pandas as pd


# In[2]:


airports = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv')


# In[3]:


airports.head()


# In[32]:


airports.isnull().sum()


# ## Northernmost airport in the United States is Dillant Hopkins Airport

# In[4]:


airports.sort_values(['lat', 'lon'], ascending = False)


# ## Easternmost Airport



# In[66]:


airports[airports.lon >=  -75.500000]


# In[26]:


airports.sort_values('lon', ascending = False)


# In[29]:


airports[(airports.lat <= 44.8131357) & (airports.lon <= -66.9627554)]


# ## On February 12th, 2013, JFK had the windiest weather

# In[33]:


weather = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv')


# In[34]:


weather.head()


# In[36]:


weather.isnull().sum()


# In[38]:


weather.dropna(how = 'all').wind_speed


# In[61]:


weather_2013 = weather[(weather.year == 2013)]


# In[62]:


weather_feb_2013 = weather_2013[(weather_2013.month == 2)]


# In[ ]:


thisweather = weather_feb_2013[(weather_feb_2013.day == 12)]


# In[63]:


thisweather = thisweather.sort_values('wind_speed', ascending = False)


# In[64]:


grouped_weather = thisweather.groupby('origin').wind_speed.max()


# In[65]:


grouped_weather.sort_values(ascending = False)


# In[ ]:




