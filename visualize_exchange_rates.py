import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Exchange_Rates_Fixed.csv')
df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'] + '-' + df['Day'].astype(str).str.zfill(2))

# Set style
sns.set_style("darkgrid")
sns.set_palette("husl")
plt.figure(figsize=(14, 8))

# Create line plot
sns.lineplot(data=df, x='Date', y='SGD_per_100_INR', linewidth=2, color='#2E86AB')

plt.title('SGD per 100 INR Exchange Rates (2006-2025)', fontsize=14, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('SGD per 100 INR')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot
plt.savefig('sgd_inr_exchange_rates.png', dpi=300, bbox_inches='tight')
plt.show()
