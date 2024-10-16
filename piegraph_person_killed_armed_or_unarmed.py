import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Calculate the percentage of police killings where people were armed
armed_status_counts = df_deaths['armed'].value_counts()
total_deaths = len(df_deaths)
percentage_armed = (armed_status_counts / total_deaths) * 100

# Create a pie chart to visualize the percentage of armed vs. unarmed
plt.figure(figsize=(8, 8))
plt.pie(percentage_armed, labels=armed_status_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'red', 'blue', 'orange', 'purple'])

# Add a title
plt.title('Percentage of Police Killings by Armed Status')

# Equal aspect ratio ensures that pie chart is drawn as a circle
plt.axis('equal')

# Show the plot
plt.tight_layout()
plt.show()
