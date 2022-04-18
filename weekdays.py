""" NumPy program to find the number of weekdays in a given month. Allow the
user to input the month and year of their choice """
def month_week_days():
    import numpy as np
    current_month = np.datetime64(input("Key year,month: "), 'M')
    next_month = current_month + np.timedelta64(1, 'M')
    weekdays = np.busday_count(current_month, next_month)
    return weekdays

print(month_week_days())