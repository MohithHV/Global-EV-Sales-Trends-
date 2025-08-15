import pandas as pd

# Load CSV
ev_data = pd.read_csv('EV_sales_data.csv')

# Preview data
print(ev_data.head())
print(ev_data.info())
# Count missing values per column
print(ev_data.isnull().sum())
# Pivot to compare sales by region and year
pivot_data = ev_data.pivot_table(
    index='Year',
    columns='Region',
    values='Sales',
    aggfunc='sum'
)

print(pivot_data.head())
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10,6))
sns.lineplot(data=pivot_data)
plt.title("EV Sales Trend by Region")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend(title='Region')
plt.show()
top_regions = ev_data[ev_data['Year'] == 2022].groupby('Region')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_regions)
