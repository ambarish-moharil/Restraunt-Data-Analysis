
# coding: utf-8

# # RESTAURANT DATA ANALYSIS

# ### OBJECTIVE:

# To analyse the timings, peak hours of the restaurant, number of people visiting the restaurant on the basis of tips, days, time etc. Give a pictorial representations of the above values on graph co-ordinates

# ### APPROACH:

# Using pandas, numpy and matplotlib we can split the data according to our liking and finding if any NaN values are present and replacing such values. Also we can then plot the bar graph or box plot of the above data.

# ### DELIVERABLES:

# 1. csv: tips.csv
# 2. box plot: boxplot grouped by day & tip
# 3. bar plot: barplot of day vs tips

# In[9]:


import pandas 
import numpy as np


# In[10]:


data=pd.read_csv('tips.csv',sep=',',encoding='latin_1') # read csv file (filepath,separator generally',',encoding standard which here is west europe)
data # print out data variable


# In[21]:


data.loc[(data["sex"]=="Female")&(data["smoker"]=="No")&(data["day"]=="Sun")&(data["time"]=="Dinner"),["sex","smoker","time","day"]] 
# Separating the data by taking female, no smoking, sunday and dinner from original data using boolean indexing method.


# In[23]:


# for female data
def num_missing(x): # Checking missing values
    return sum(x.isnull())

print "Missing Values per Columns:"
print data.apply(num_missing, axis=0) # apply returns some value after passing each column(axis=0 i.e. column) of adata frame with some function(i.e. missing values here)

print "Missing Values per Rows:"
print data.apply(num_missing, axis=1).head() # axis=1 means rows


# In[24]:


data.loc[(data["sex"]=="Male")&(data["smoker"]=="No")&(data["day"]=="Sun")&(data["time"]=="Dinner"),["sex","smoker","time","day"]]
# Separating the data by taking male, no smoking, sunday and dinner from original data using boolean indexing method


# In[26]:


# for male data
def num_missing(x):
    return sum(x.isnull())

print "Missing Values per Columns For Male:"
print data.apply(num_missing, axis=0)

print "Missing Values per Rows For Male:"
print data.apply(num_missing, axis=1).head()


# In[27]:


# determine pivot table
impute_grps=data.pivot_table(values=["tip"], index=["sex","smoker","time","day"], aggfunc=np.mean)
# using pandas we can create MS Excel style pivot tables. for instance a key column is 'tip' which will be imputed using mean amount of each sex, smoker, time and day. 
print impute_grps


# In[28]:


# sorting data
data_sort=data.sort_values(['tip','total_bill'], ascending=False) 
# pandas allow easy sorting based on multiple columns.
data_sort[['tip','total_bill']].head(10) # .head(10) will only take 10 values to diplay


# In[31]:


#plotting boxplot
import matplotlib.pyplot as plt
data.boxplot(column="tip",by="day")


# In[32]:


# plotting histogram
data.hist(column="tip",by="day",bins=30)


#                                                                                        DONE BY: SOURABH SHRIPAD NAIK
