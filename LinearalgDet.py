"""import numpy 
#The first N line contains the integer .
N = int(input())

#The next  lines contains the  space separated elements of array .

arr = numpy.array([input().split() for _ in range(N)],float)

#print the determinant of arr
#2
#1.1 1.1
#1.1 1.1
print(round(numpy.linalg.det(arr), 2))

#Output
#0.0"""

import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

#A single line of input containing the space separated month, day and year, respectively, in MM DD year format.
#08 05 2015
#Output
#WEDNESDAY
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())  #calendar.day_name is used to get the name of the day of the week.
#calendar.weekday() is used to get the day of the week.
# .weekday() is used to get the day of the week.   
 # .upper() is used to convert the output to uppercase letters.
