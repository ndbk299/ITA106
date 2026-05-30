import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

# Bài 1
print("Bài 1:")

np.random.seed(42)
data = pd.DataFrame({
    'Age': np.random.randint(18, 70, size=100),
    'Income': np.random.randint(30000, 100000, size=100),
    'Spending Score': np.random.randint(1, 100, size=100),
})
print(data.head())

# Histogram 
data.hist(bins=20, figsize=(10, 6))
plt.tight_layout()
plt.show()

# Density Plot (KDE)
for feature in data.columns:
    sns.kdeplot(data[feature], label=feature, fill=True)
plt.title('Density Plots')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.show()

# Box Plot
sns.boxplot(data=data)
plt.title('Box Plots')
plt.show()  

# Bài 2
print("Bài 2:")
ticker = 'AAPL'
stock = yf.download(ticker, start="2022-01-01", end="2024-01-01")
stock.head()

# Line Chart cho giá đóng cửa
plt.figure(figsize=(12, 6))
plt.plot(stock.index, stock['Close'], label='Close Price')
plt.title(f'{ticker} Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Moving Average (trung bình động)
stock["MA50"] = stock["Close"].rolling(window=50).mean()
stock["MA200"] = stock["Close"].rolling(window=200).mean()
plt.figure(figsize=(12, 6))
plt.plot(stock.index, stock['Close'], label='Close Price')
plt.plot(stock.index, stock['MA50'], label='50-Day MA')
plt.plot(stock.index, stock['MA200'], label='200-Day MA')
plt.title(f'{ticker} Closing Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Bài 3
print("Bài 3:")

data2 = pd.DataFrame({
    'Age': np.random.randint(18, 70, size=100),
    'Income': np.random.randint(30000, 100000, size=100),
    'Spending Score': np.random.randint(1, 100, size=100),
})
print(data2.head())

# Box Plot
sns.boxplot(data=data2)
plt.title('Box Plots')
plt.show()  

# Outliers
for feature in data2.columns:
    Q1 = data2[feature].quantile(0.25)
    Q3 = data2[feature].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data2[(data2[feature] < lower_bound) | (data2[feature] > upper_bound)]
    print(f"Outliers in {feature}:\n{outliers}\n")

# Bài 4
print("Bài 4:")

# Tính ma trận tương quan (correlation matrix)
corr_matrix = data2.corr()
corr_matrix

# Heatmap truc quan hóa ma trận tương quan
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
plt.show()


