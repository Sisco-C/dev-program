import numpy as np
  
# we use the np.datetime64 
today = np.datetime64('today', 'D')
print("Today: ", today)
  
# for yesterday, we subtract a day
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  
print("Yesterday: ", yesterday)
  
# for tomorrow we add a day
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  
print("Tomorrow: ", tomorrow)