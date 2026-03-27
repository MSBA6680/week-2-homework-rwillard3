import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read Costco data from Excel
df = pd.read_excel("CostcoHW2.xlsx")

# Clean column names (removes hidden spaces)
df.columns = df.columns.str.strip()

# Convert Date column and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df.set_index('Date', inplace=True)

# Calculate daily returns and annualized volatility
df['Returns'] = df['Price'].pct_change()
df['Volatility'] = df['Returns'].rolling(window=252).std() * np.sqrt(252)

# Plot everything
plt.figure(figsize=(14, 12))

# Plot Costco prices
plt.subplot(3, 1, 1)
plt.plot(df.index, df['Price'], label='Costco Prices', color='blue')
plt.title('Costco Stock Prices')
plt.ylabel('Price')
plt.legend()

# Plot returns
plt.subplot(3, 1, 2)
plt.plot(df.index, df['Returns'], label='Daily Returns', color='green')
plt.title('Costco Daily Returns')
plt.ylabel('Return')
plt.legend()

# Plot annualized volatility
plt.subplot(3, 1, 3)
plt.plot(df.index, df['Volatility'], label='Annualized Volatility', color='red')
plt.title('Costco Annualized Volatility')
plt.ylabel('Annualized Volatility')
plt.xlabel('Year')
plt.legend()

plt.tight_layout()
plt.savefig("CostcoHW2_plots.png", bbox_inches="tight")
print("Plot saved as CostcoHW2_plots.png")