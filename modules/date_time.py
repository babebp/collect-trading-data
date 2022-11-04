from datetime import date
from datetime import datetime
import calendar

class GetTime:
    def get_time(self):
            my_date = date.today()
            day_of_week = calendar.day_name[my_date.weekday()] 
            return day_of_week, datetime.today().strftime('%Y-%m-%d'), datetime.today().strftime('%H:%M:%S')