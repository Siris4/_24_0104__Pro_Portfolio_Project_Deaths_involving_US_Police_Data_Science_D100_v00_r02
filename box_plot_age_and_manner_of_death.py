import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Create a box plot showing the age and manner of death, broken out by gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='manner_of_death', y='age', hue='gender', data=df_deaths, palette='Set2')

# Add labels and a title
plt.xlabel('Manner of Death')
plt.ylabel('Age')
plt.title('Box Plot of Age and Manner of Death by Gender')

# Show the plot
plt.tight_layout()
plt.show()
