import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import the full_data.csv in this file
os.chdir("/Users/chenyoulin/Desktop/great")
import pandas as pd

# name this file
covid_data = pd.read_csv("full_data.csv")

# the second column from every 100th row from the first 1000 rows
# the preceding row represent the row in parentheses
data = covid_data.iloc[0:1001:100, 1]
data
# print the data
print(data)


# This is the original formula given
covid_data.loc[0:81, "total_cases"]
# Boolean to show “total cases” for all rows corresponding to Afghanistan
# index the location of Afdhanistan and find it
covid_data.loc[covid_data.loc[:, "location"]=="Afghanistan", "total_cases"]



# Find the location of new_cases and new_deaths, using function to determine its rows and columns
new_data=covid_data.loc[covid_data.loc[:, "data" == "2020-03-31", ["location", "new_cases", "new_deaths"]]]
# Use the head command to view the new_data
new_data.head()
# Calculate the mean of new_cases and new_deaths in new_data
np.mean(new_data.loc[:, ["new_cases", "new_deaths"]])
# print the result
print()



# Find the location of new_cases and new_deaths, using function to determine its rows and columns
new_data = covid_data.loc[covid_data['date'] == '2020-03-31', ['location', 'new_cases', 'new_deaths']]
# Draw boxplot about new_cases and  new_deaths, values represent the values inside
plt.boxplot(new_data[['new_cases', 'new_deaths']].values)
# Name the title New Cases and Deaths on 31 March 2020
plt.title("New Cases and Deaths on 31 March 2020")
# Set the x-ais to Cases and Deaths
plt.xlabel('Cases, Deaths')
# Get the boxplot
plt.show()


# Made another object called world_dates and select new_cases
world_new_cases=covid_data['new_cases']
# Made another object called world_dates and select new_cases
world_new_deaths=covid_data['new_deaths']
# set the plot and variable is new cases and use b+
plt.plot(world_dates, world_new_cases, 'b+',label="new cases")
# Rotate the x-axis abscissa 90 degrees and set the font size to 4
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90,fontsize=4)
# The variable of this plot is new deaths and use r+
plt.plot(world_dates, world_new_deaths, 'r+',label="new deaths")
# Rotate the x-axis abscissa 90 degrees and set the font size to 4
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90,fontsize=4)
# Name the title of plot to new cases and new deaths worldwide over time
plt.title("new cases and new deaths worldwide over time")
# SHow the plot
plt.show()



# How have new cases and total cases developed over time in the UK?
# Extract information from the UK and use it as an index
UK_data = covid_data.loc[covid_data['location'] == 'United Kingdom']
# Draw a plot diagram and target total_cases
plt.plot(UK_data['date'], UK_data['total_cases'], label='Total Cases')
# Draw a plot diagram and target new_cases,see the trend of change
plt.plot(UK_data['date'], UK_data['new_cases'], label='New Cases')
# The title of plot id COVID-19 Cases in the UK
plt.title('COVID-19 Cases in the UK')
# The x label variable is the Date
plt.xlabel('Date')
# The y label variable is Number of Cases
plt.ylabel('Number of Cases')
# Rotate the x-axis abscissa 90 degrees and set the font size to 4
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90,fontsize=4)
# Show the plot diagram
plt.show()
