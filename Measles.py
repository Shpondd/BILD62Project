#!/usr/bin/env python
# coding: utf-8

# # Measles Analysis 
# An indepth analysis of the Measles pandemic in the United States based on data from the CDC

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt 
import os


# In[2]:


print(os.getcwd())


# Data used in our analysis was collected from the following webistes:
# 
# - https://www.cdc.gov/measles/data-research/index.html#cdc_data_surveillance_section_5-yearly-measles-cases
# - https://www.cdc.gov/mmwr/volumes/73/wr/mm7314a1.htm
# - https://dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/measles.html

# The data files used in the overview portion of the analysis are imported and listed below:

# In[4]:


yearly_cases_data = pd.read_csv('/home/shpond/BILD62_FA24/MeaslesProj/Data/YC.csv', delimiter=',')
Illinois_overview = pd.read_csv('/home/shpond/BILD62_FA24/MeaslesProj/Data/Illinois.csv', delimiter=',')
International_data = pd.read_csv('/home/shpond/BILD62_FA24/MeaslesProj/Data/International.csv', delimiter=',')


# Following code box is used for confirming that the files were imported correctly and looking into the structuring of the files for later use

# In[84]:


display(yearly_cases_data)
display(Illinois_overview)
display(International_data)


# Next, we will analyze each set of data separately starting with the yearly measles cases in the United States from 1985 to 2024.

# I want to graph this data to observe the change in number of cases throughout the years. 

# In[85]:


fig =plt.figure()
plt.plot(yearly_cases_data['Year'], yearly_cases_data['Cases']) #Plotting the cases by year
plt.xlabel('Years') #Set a x label
plt.ylabel('Number of Cases') #Set a y label 
plt.title('Yearly Cases in the United States from 1985 to 2024') #Title the figure
plt.xlim(1985, 2024) #Set the x axis limit, before it went to 2025 and I did not want that 

plt.show()


# Next, I want to look at the yearly number of cases just for Illinois:

# In[86]:


Illinois_data = ['Year', 'Cases'] #Choosing the column heads that I want
Illinois_relevant = Illinois_overview[Illinois_data] #Setting the data to be only the relevant columns
display(Illinois_relevant) #checking that it worked 


# In[87]:


# fig = plt.figure()
plt.plot(Illinois_relevant['Year'], Illinois_relevant['Cases']) #plotting the number of cases throughout the years
plt.xlabel('Year') #Set x label 
plt.ylabel('Number of cases') #Set y label 
plt.title('Yearly Cases in Illinois from 1917 to 2024') #Title the graph

plt.show()


# Next, I want to look at the overall international data.

# In[88]:


Regions = ['Eastern Mediterranean', 'African', 'European', 'South-East Asia', 'Americas', 'Western Pacific'] #Setting the regions that we are looking at
International_Regions = International_data[Regions] #Connecting these regions to the data 
fig = plt.figure()
plt.plot(International_data['Years'], International_Regions) # Graphing the number of cases over the years for each region
plt.xlabel('Year') #Set x label 
plt.ylabel('Number of cases') #Set y label 
plt.legend(Regions) #Make a legend
plt.title('Yearly Cases internationally from 2020 to 2024') #Title the graph
plt.xticks([2020, 2021, 2022, 2023, 2024]) #Set the x axis ticks, was not whole numbers before

plt.show()


# And finally, I want to compare the data from the overall United States and the data from just Illinois. 

# In[89]:


fig = plt.figure()
plt.plot(Illinois_relevant['Year'], Illinois_relevant['Cases']) #Plotting Illinois
plt.plot(yearly_cases_data['Year'], yearly_cases_data['Cases']) #Plotting United States
plt.legend(['Illinois data', 'United States data']) #Legend to label both
plt.xlabel('Year') #Set the x label 
plt.ylabel('Number of cases') #Set the y label 
#Next, I want to add labels for the important milestones
plt.annotate(
    "First measles vaccines \napproved in US",  
    xy=(1963, 11862),         # Point to annotate
    xytext=(1945, 65000),     # Position for the annotation text
    arrowprops=dict(facecolor='green', shrink=0.05, width=1, headwidth=8))
plt.annotate(
    "Large outbreak among \nvaccinated children leading \nto second dose of MMR",  
    xy=(1989, 24000),         
    xytext=(1970, 45000),    
    arrowprops=dict(facecolor='green', shrink=0.05, width=1, headwidth=8))

plt.show()


# In[ ]:




