#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[30]:


# load in master csv
df = pd.read_csv("passplaysfiltered.csv")


# In[27]:


# rename column name to match yearly data
# remove non letter characters and replace with a space
df.rename(columns = {"passer_player_name": "Player"}, inplace=True)
df["Player"] = df["Player"].str.replace(r"[^a-zA-Z]", " ", regex=True)
print(df["Player"])


# In[26]:


# load in yearly data, only loading in the important columns using usecols
# the data had unnecessary row at begining of csv, so skiprows=1 removes the first row
columns = ["Player", "PktTime"]
df_2021 = pd.read_csv("2021 Advanced Passing Stats.csv", skiprows=1, usecols=columns)
df_2022 = pd.read_csv("2022 Advanced Passing Stats.csv", skiprows=1, usecols=columns)
df_2023 = pd.read_csv("2023 Advanced Passing Stats.csv", skiprows=1, usecols=columns)
print(df_2022)


# In[25]:


# data cleaning
# remove non letter characters
df_2021["Player"] = df_2021["Player"].str.replace(r"[^a-zA-Z\s]", "", regex=True)
df_2022["Player"] = df_2022["Player"].str.replace(r"[^a-zA-Z\s]", "", regex=True)
df_2023["Player"] = df_2023["Player"].str.replace(r"[^a-zA-Z\s]", "", regex=True)
print(df_2022)


# In[24]:


# format player column to match name format from the master dataset
df_2021["Player"] = df_2021["Player"].apply(lambda x: f"{x.split()[0][0]} {x.split()[1]}" if len(x.split()) > 1 else x)
df_2022["Player"] = df_2022["Player"].apply(lambda x: f"{x.split()[0][0]} {x.split()[1]}" if len(x.split()) > 1 else x)
df_2023["Player"] = df_2023["Player"].apply(lambda x: f"{x.split()[0][0]} {x.split()[1]}" if len(x.split()) > 1 else x)
print(df_2022)


# In[22]:


# split df into three datasets based on year
# this will make merging the PkTime datasets easier
df_21_tmp = df[df['season'] == 2021]
df_22_tmp = df[df['season'] == 2022]
df_23_tmp = df[df['season'] == 2023]


# In[21]:


# merge datasets based on Quarterback(player) name
# three different merged datasets based on year(season)
df_21_merge = pd.merge(df_21_tmp, df_2021, on='Player', how='left')
df_22_merge = pd.merge(df_22_tmp, df_2022, on='Player', how='left')
df_23_merge = pd.merge(df_23_tmp, df_2023, on='Player', how='left')


# In[20]:


# combine all the merge datasets together to make the master dataset
df_combined = pd.concat([df_21_merge, df_22_merge, df_23_merge], axis=0, ignore_index=True)


# In[ ]:




