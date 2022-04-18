""" NumPy program to get the dates of yesterday, today and tomorrow """

import numpy as np
def dates():
  today = np.datetime64('today', 'D')
  yesterday = today - np.timedelta64(1, 'D')
  tomorrow = today + np.timedelta64(1, 'D')
  return np.datetime_as_string(today), np.datetime_as_string(yesterday), np.datetime_as_string(tomorrow)


print(dates())
