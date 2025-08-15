powertrain_sales = ev_data.groupby('Powertrain')['Sales'].sum()
print(powertrain_sales)

# Plot comparison
powertrain_sales.plot(kind='bar', color=['blue', 'green'])
plt.title("Total EV Sales by Powertrain")
plt.ylabel("Sales")
plt.show()
