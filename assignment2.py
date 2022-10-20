import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Question 1
# Using NumPy create random vector of size 15 having only Integers in the range 1-20
x = np.random.randint(1, 20, 15)
print(x)
# Reshape the array to 3 by 5
y = np.reshape(x, (3, 5))
print(y)
# Replace the max in each row by 0
max_1 = np.amax(y, axis=1)
max_1 = max_1[:, None]
z = np.where(y == max_1, 0, y)
print(z)

# Question 2
# Read the provided CSV file ‘data.csv’.
data = pd.read_csv("S:/data.csv")
# Show the basic statistical description about the data.
data.head()
data.describe()
# Check if the data has null values.(Replace the null values with the mean)
data = data.fillna(data.mean())
# Select at least two columns and aggregate the data using: min, max, count, mean.
print(data[['Maxpulse', 'Calories']].agg(['min', 'max', 'mean', 'count']))
# Filter the dataframe to select the rows with calories values between 500 and 1000.
print(data[(data.Calories < 1000) & (data.Calories > 500)])
# Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print(data[(data.Calories > 500) & (data.Pulse < 100)])
# Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.
df_modified = pd.DataFrame(data, columns=['Duration', 'Pulse', 'Calories'])
print(df_modified.head())
# Delete the “Maxpulse” column from the main df dataframe
del data['Maxpulse']
print(data.head())
# Convert the datatype of Calories column to int datatype
data['Calories'] = data['Calories'].astype("int")
print(data['Calories'].dtypes)
# Using pandas create a scatter plot for the two columns (Duration and Calories).
data.plot.scatter(x='Duration', y='Calories')
plt.show()

# Question 3
# Write a Python programming to create a below chart of the popularity of programming Languages.
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1, 0, 0, 0, 0, 0)
plt.pie(popularity, explode=explode, labels=languages, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
