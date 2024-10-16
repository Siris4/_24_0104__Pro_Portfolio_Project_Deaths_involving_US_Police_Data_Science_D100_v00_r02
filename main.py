import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the racial data
file_path_race = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Share_of_Race_By_City.csv'
df_race = pd.read_csv(file_path_race, encoding='ISO-8859-1')

# Check the first few rows to understand the structure
print(df_race.head())

# Convert the relevant race columns to numeric, forcing invalid data to NaN
race_columns = ['share_white', 'share_black', 'share_native_american', 'share_asian', 'share_hispanic']
df_race[race_columns] = df_race[race_columns].apply(pd.to_numeric, errors='coerce')

# Check if there are any invalid (non-numeric) entries
print(df_race[race_columns].dtypes)

# Now group by state and calculate the mean for the race columns
df_state_race = df_race.groupby('Geographic area')[race_columns].mean().reset_index()

# Set the state names as the index for easy plotting
df_state_race.set_index('Geographic area', inplace=True)

# Plot a stacked bar chart to show the share of racial demographics in each state
df_state_race.plot(kind='bar', stacked=True, figsize=(12, 8))

# Add labels and a title
plt.xlabel('US State')
plt.ylabel('Population Share (%)')
plt.title('Racial Demographics in Each US State')
plt.legend(title='Race', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()
