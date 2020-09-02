import pandas as pd


data = pd.date_range(start='1961-04-12', end='1969-07-21', freq='D')
# DatetimeIndex(['1961-04-12', '1961-04-13', '1961-04-14', '1961-04-15',
#                '1961-04-16', '1961-04-17', '1961-04-18', '1961-04-19',
#                '1961-04-20', '1961-04-21',
#                ...
#                '1969-07-12', '1969-07-13', '1969-07-14', '1969-07-15',
#                '1969-07-16', '1969-07-17', '1969-07-18', '1969-07-19',
#                '1969-07-20', '1969-07-21'],
#               dtype='datetime64[ns]', length=3023, freq='D')

s = pd.Series(data)

len(s)
# 3023

s.__len__()
# 3023