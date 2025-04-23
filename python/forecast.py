 
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulated sales data
data = pd.read_json('data/sales.json')
data['timestamp'] = pd.to_datetime(data['sale_date'])
data = data.groupby(data['timestamp'].dt.date)['price'].sum().reset_index()
data.columns = ['ds', 'y']

# Forecast using linear regression
data['ds_ordinal'] = pd.to_datetime(data['ds']).map(pd.Timestamp.toordinal)
X = data[['ds_ordinal']]
y = data['y']
model = LinearRegression().fit(X, y)
data['y_pred'] = model.predict(X)

# Plot
plt.plot(data['ds'], data['y'], label='Actual')
plt.plot(data['ds'], data['y_pred'], label='Forecast')
plt.legend()
plt.savefig('forecast.png')
