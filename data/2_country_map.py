import pandas as pd
import os

# Define the folder containing the CSV files
file = 'merged_happiness_report.csv'
folder = '1_stage_merge'

country_mapping = {
    'United States': 'United States of America',
    'South Sudan': 'S. Sudan',
    'Congo (Kinshasa)': 'Dem. Rep. Congo',
    'Central African Republic': 'Central African Rep.',
}

df = pd.read_csv(os.path.join(folder, file))

df['Country'] = df['Country'].replace(country_mapping)

# Save the merged DataFrame to a CSV file
df.to_csv('2_stage_country/countries_renamed_happiness_report.csv', index=False)
