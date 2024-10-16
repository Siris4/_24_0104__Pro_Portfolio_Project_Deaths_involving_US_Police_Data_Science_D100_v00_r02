import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by race and count the number of deaths for each race
deaths_by_race = df_deaths['race'].value_counts()

# Create a donut chart
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(deaths_by_race, labels=deaths_by_race.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))

# Add a circle in the center to make it a donut chart
centre_circle = plt.Circle((0, 0), 0.70, color='white', fc='white', linewidth=1.25)
plt.gca().add_artist(centre_circle)

# Map race codes to full race names
race_labels = {
    'W': 'White',
    'B': 'Black',
    'H': 'Hispanic',
    'A': 'Asian',
    'N': 'Native American',
    'O': 'Other',
    'Unknown': 'Unknown'
}

# Add a legend with the full race names spelled out
plt.legend(wedges, [race_labels.get(race, race) for race in deaths_by_race.index], title="Race", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Add a title
plt.title('Percentage of People Killed by Race in the US (Police Fatalities)')

# Show the plot
plt.tight_layout()
plt.show()
