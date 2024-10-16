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

# Create a histogram and KDE plot of the age distribution
plt.figure(figsize=(10, 6))

# Plot histogram
sns.histplot(df_deaths['age'], bins=20, kde=False, color='blue', alpha=0.6, label='Histogram')

# Plot KDE
sns.kdeplot(df_deaths['age'], color='red', label='KDE')

# Add labels and a title
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Distribution of Ages of People Killed by Police')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
