import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by race and count the number of deaths for each race
deaths_by_race = df_deaths['race'].value_counts()

# Create a bar chart to show the total number of people killed by race
plt.figure(figsize=(8, 6))
plt.bar(deaths_by_race.index, deaths_by_race.values, color='skyblue')

# Add labels and a title
plt.xlabel('Race')
plt.ylabel('Number of Deaths')
plt.title('Total Number of People Killed by Race (Police Fatalities)')

# Show the plot
plt.tight_layout()
plt.show()
