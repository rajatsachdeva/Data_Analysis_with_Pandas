import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

# Specify the start and end date for which the data will be fetched
start = datetime.datetime(2010, 1, 1)
end   = datetime.datetime(2017, 1, 1)

# Fetch data from yahoo finance for apple stock 
df = web.DataReader("AAPL", "yahoo", start, end)

# Get the first five entries 
print(df.head())

# Get the last five entries
print(df.tail())

# plot Ajusted close data 
df['Adj Close'].plot()

# display the plotted graph
plt.show()