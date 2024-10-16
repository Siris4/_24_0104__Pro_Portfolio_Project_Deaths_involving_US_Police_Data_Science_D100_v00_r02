import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Remove any rows with missing or invalid age data
df_deaths = df_deaths[df_deaths['age'].notna()]

# Filter out rows where race information is missing
df_deaths = df_deaths[df_deaths['race'].notna()]

# Create a list of unique races to loop through
races = df_deaths['race'].unique()

# Set up the plot figure
plt.figure(figsize=(10, 6))

# Create a KDE plot for each race
for race in races:
    sns.kdeplot(df_deaths[df_deaths['race'] == race]['age'], label=race)

# Add labels and a title
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('KDE Plot of Age Distribution by Race (Police Fatalities)')

# Add a legend
plt.legend(title='Race')

# Show the plot
plt.tight_layout()
plt.show()
