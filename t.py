from datetime import timedelta
from datetime import date
firstDay= date(2016,2,1)
for i in range(10):
    current_date = firstDay + timedelta(1) * i
    print(current_date)