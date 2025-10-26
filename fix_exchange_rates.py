import pandas as pd
import re

# Read the file
with open('Exchange Rates (1).csv', 'r') as f:
    content = f.read()

# Remove header text and footer notes
lines = content.split('\n')
data_lines = []
current_year = None
current_month = None

for line in lines:
    # Skip header lines and notes
    if (line.startswith('MAS:') or line.startswith('Exchange Rates') or 
        line.startswith('Jan 2006') or line.startswith('"*') or 
        line.strip() == '' or line.startswith('End of Period')):
        continue
    
    # Split by comma
    parts = [p.strip() for p in line.split(',')]
    
    if len(parts) >= 4:
        year, month, day, rate = parts[0], parts[1], parts[2], parts[3]
        
        # Update current year if not empty
        if year and year.isdigit():
            current_year = year
        
        # Update current month if not empty
        if month and not month.isdigit():
            current_month = month
        
        # Only add rows with actual data (day and rate)
        if day and rate and day.isdigit():
            data_lines.append([current_year, current_month, day, rate])

# Create DataFrame and save
df = pd.DataFrame(data_lines, columns=['Year', 'Month', 'Day', 'SGD_per_100_INR'])
df.to_csv('Exchange_Rates_Fixed.csv', index=False)
print(f"Fixed CSV created with {len(df)} rows")
