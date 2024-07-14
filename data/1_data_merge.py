import pandas as pd
import os

# Define the folder containing the CSV files
folder = 'raw'

# Define the file names
files = ['2015.csv', '2016.csv', '2017.csv', '2018.csv', '2019.csv']

# Define a mapping for the column names to standardize them
column_mapping = {
    'Country': 'Country',
    'Country or region': 'Country',
    'Region': 'Region',
    'Overall rank': 'Happiness Rank',
    'Happiness Rank': 'Happiness Rank',
    'Happiness.Rank': 'Happiness Rank',
    'Happiness Score': 'Happiness Score',
    'Happiness.Score': 'Happiness Score',
    'Score': 'Happiness Score',
    'Standard Error': 'Standard Error',
    'Economy (GDP per Capita)': 'GDP per capita',
    'Economy..GDP.per.Capita.': 'GDP per capita',
    'Family': 'Social support',
    'Health (Life Expectancy)': 'Healthy life expectancy',
    'Health..Life.Expectancy.': 'Healthy life expectancy',
    'Freedom': 'Freedom to make life choices',
    'Trust (Government Corruption)': 'Perceptions of corruption',
    'Trust..Government.Corruption.': 'Perceptions of corruption',
    'Generosity': 'Generosity',
    'Dystopia Residual': 'Dystopia Residual',
    'Dystopia.Residual': 'Dystopia Residual',
    'Lower Confidence Interval': 'Lower Confidence Interval',
    'Upper Confidence Interval': 'Upper Confidence Interval',
    'Whisker.high': 'Upper Confidence Interval',
    'Whisker.low': 'Lower Confidence Interval',
}

country_mapping = {
    'United States': 'United States of America',
    'South Sudan': 'S. Sudan'
}

# Initialize an empty DataFrame
merged_df = pd.DataFrame()

# Process each file
for file in files:
    # Extract the year from the file name
    year = file.split('.')[0]
    
    # Read the CSV file
    df = pd.read_csv(os.path.join(folder, file))
    
    # Rename the columns
    df = df.rename(columns=column_mapping)
    
    # Drop the 'Lower Confidence Interval' and 'Upper Confidence Interval' columns if they exist
    df = df.drop(columns=['Lower Confidence Interval', 'Upper Confidence Interval'], errors='ignore')
    
    # Add the year column
    df['Year'] = year
    
    # Ensure 'Year' is the first column
    df = df[['Year'] + [col for col in df.columns if col != 'Year']]
    
    # Append the data to the merged DataFrame
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save the merged DataFrame to a CSV file
merged_df.to_csv('1_stage_merge/merged_happiness_report.csv', index=False)
