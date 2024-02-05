#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv('C:/Users/27818/Downloads/movie_dataset.csv')


# In[4]:


df.head()


# In[5]:


df.isnull()


# In[6]:


df = df.dropna()


# In[7]:


df.duplicated()


# In[8]:


df = df.drop_duplicates()


# In[20]:


highest_rated_movie = df.loc[df['Rating'].idxmax(), 'Title']
print("Highest rated movie:", highest_rated_movie)


# In[ ]:





# In[21]:


average_revenue_all = df['Revenue (Millions)'].mean()
print("Average revenue of all movies:", average_revenue_all)


# In[22]:


average_revenue_2015_2017 = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]['Revenue (Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_2017)


# In[23]:


movies_2016 = df[df['Year'] == 2016].shape[0]
print("Number of movies released in 2016:", movies_2016)


# In[24]:


movies_nolan = df[df['Director'] == 'Christopher Nolan'].shape[0]
print("Number of movies directed by Christopher Nolan:", movies_nolan)


# In[30]:


high_rated_movies = df[df['Rating'] >= 8.0] 
num_high_rated_movies = len(high_rated_movies)
print("Number of movies with a rating of at least 8.0:", num_high_rated_movies)


# In[33]:


year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()
print("Year with the highest average rating:", year_highest_avg_rating)


# In[34]:


movies_2006 = df[df['Year'] == 2006]
movies_2016 = df[df['Year'] == 2016]


# In[35]:


percentage_increase = ((len(movies_2016) - len(movies_2006)) / len(movies_2006)) * 100
print("Percentage increase in the number of movies between 2006 and 2016:", percentage_increase)


# In[37]:


unique_genres = df['Genre'].str.split(', ').explode().nunique()
print("Number of unique genres in the dataset:", unique_genres)


# In[38]:


correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)


# In[ ]:




