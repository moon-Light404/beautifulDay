import time
from datetime import datetime
time1 = datetime.now()
def midfind(list,n):
    len1 = len(list)
    low = 0
    high = len1 - 1
    while(low <= high):
        mid = low + (high - low)//2
        if n > list[mid]:
            low += 1
        elif n < list[mid]:
            high -= 1
        else:
            return mid
list1 = [1,2,3,4,0,27,5,45,5,5,8,9,45,12,7,4,6,9,1,3,0,1,4,5,8,7,9]
print(midfind(list1,45))
time2 = datetime.now()
print((time2 - time1).total_seconds())