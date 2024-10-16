import pandas as pd

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Filter the dataset to include only those under 25 years old
under_25 = df_deaths[df_deaths['age'] < 25]

# Calculate the percentage of people killed who were under 25 years old
total_deaths = len(df_deaths)
under_25_percentage = (len(under_25) / total_deaths) * 100

# Print the percentage of people killed who were under 25
print(f"Percentage of people killed under 25 years old: {under_25_percentage:.2f}%")
