#!/usr/bin/env python
# coding: utf-8

# # PyCity Schools Analysis
# 
# * One variable that stayed consistent was the correlation between the budget and the number of students, regardless of whether the school was of the type "District" or "Charter", which suggests that the average amount of money supposedly devoted per child was consistent as well.
# 
# * The size of the school did not have a significant effect on the average math or reading scores.

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[9]:


# Dependencies and Setup
import pandas as pd
import numpy as np


# In[8]:


# File to Load 
schools_data = "Resources/schools_complete.csv"
students_data = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames

schools_data_pd = pd.read_csv(schools_data)
schools_data_pd.head()
students_data_pd = pd.read_csv(students_data)
students_data_pd.head()

# Combine the data into a single dataset
school_data_complete = pd.merge(students_data, schools_data, how="left", on=["school_name", "school_name"])
school_data_complete_pd = pd.read_csv(school_data_complete)

school_data_complete_pd.head()


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[ ]:


school_count= len(school_data_complete_df["school_name"].value_counts())
student_count = len(school_data_complet_df["student_name"].value_counts())

Budget_Total = df["budget"].sum

print(Budget_Total)

average_math = df["math_score"].mean()
average_reading = df["reading_score"].mean()
df1['average_math'] = pd.Series(np.random.randn(sLength), index=df1.index)
df2['average_reading'] = pd.Series(np.random.randn(sLength), index=df1.index)
overall_passing_rate =school_data_complete_pd["average_math" + "average_reading"]/2
school_data_complete_pd["Overall Passing Rate"] = overall_passing_rate



# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results
# school_data_complete_pd.head()
# school_data_complete_pd.describe
# 
# 

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[ ]:


passing_overall_df = school_data_complete_pd.sort_values("overall_passing_rate", ascending=False)
passing_overall_df.head


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[ ]:


not_passing_overall_df = school_data_complete_pd.sort_values("overall_passing_rate")
not_passing_overall_df.head


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[ ]:





# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[ ]:





# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[ ]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[ ]:





# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


size_bins = [0,500, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:





# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[ ]:


size_bins = [0,500, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:

