# Using pandas data frame to draw the graph
# auhtor: AAJ 
# Date: 31/05/2020
# Tested on repl and IDLE windows 10

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

response = requests.get('https://pomber.github.io/covid19/timeseries.json').json()

country = response['Australia']
df = pd.DataFrame(country,columns=['date','confirmed','deaths','recovered'])
print(df)

# draw a line graph between date and confirmed
df.plot(x ='date', y='confirmed', kind = 'line')
plt.show()
