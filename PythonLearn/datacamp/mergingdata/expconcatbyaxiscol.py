# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max,weather_mean],axis='columns')

# Print weather
print(weather)

'''

 Max TemperatureF  Mean TemperatureF
Apr              89.0          53.100000
Aug               NaN          70.000000
Dec               NaN          34.935484
Feb               NaN          28.714286
Jan              68.0          32.354839
Jul              91.0          72.870968
Jun               NaN          70.133333
Mar               NaN          35.000000
May               NaN          62.612903
Nov               NaN          39.800000
Oct              84.0          55.451613
Sep               NaN          63.766667

'''