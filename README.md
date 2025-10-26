# SGD-INR Exchange Rates Dataset

Historical exchange rates data for Singapore Dollar (SGD) per 100 Indian Rupees (INR) from January 2006 to October 2025.

## Data Source
[Monetary Authority of Singapore (MAS) Financial Database](https://eservices.mas.gov.sg/statistics/msb/exchangerates.aspx)


## Files
- `raw_data.csv` - Original data from MAS
- `Exchange_Rates_Fixed.csv` - Cleaned dataset with filled columns
- `fix_exchange_rates.py` - Data cleaning script

## Dataset Details
- **Period**: January 2006 - October 2025
- **Records**: 4,972 daily exchange rates
- **Format**: SGD per 100 INR
- **Update Frequency**: Daily (business days)

## Usage
```python
import pandas as pd
df = pd.read_csv('Exchange_Rates_Fixed.csv')
```

## Current Rate (Oct 2025)
~1.48 SGD per 100 INR
