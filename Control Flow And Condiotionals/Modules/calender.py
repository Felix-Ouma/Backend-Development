import sys
locations = sys.path
print(locations)
for i in locations:
 print(i)

import calendar
leapdays = calendar.leapdays(2000, 2064)
print(leapdays)

isleap = calendar.isleap(2021)
print(isleap)


import time
daylight = time.daylight
print(daylight)
