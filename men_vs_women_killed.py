import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by gender and count the number of deaths for each
deaths_by_gender = df_deaths['gender'].value_counts()

# Create a bar chart comparing the number of deaths between men and women
plt.figure(figsize=(6, 6))
plt.bar(deaths_by_gender.index, deaths_by_gender.values, color=['blue', 'pink'])

# Add labels and a title
plt.xlabel('Gender')
plt.ylabel('Number of Deaths')
plt.title('Total Number of Deaths by Gender (Police Fatalities)')

# Show the plot
plt.tight_layout()
plt.show()
