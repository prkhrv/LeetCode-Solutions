# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from datetime import datetime, timedelta

intervals = [["12:30-18:00"], ["12:15-19:00"], ["00:00-18:00"]]

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%H:%M') for dt in 
       datetime_range(datetime(2016, 9, 1), datetime(2016, 9, 2), 
       timedelta(minutes=15))]

ints = []
for i in range(0,len(dts)-1):
    interval = dts[i]+"-"+dts[i+1]
    ints.append(interval)
# print(ints)

def check_free(interval,free):
    flag = 0
    interval = interval.split("-")
    t1 = timedelta(hours=int(interval[0].split(":")[0]), minutes=int(interval[0].split(":")[1]))
    t2 = timedelta(hours=int(interval[1].split(":")[0]), minutes=int(interval[1].split(":")[1]))
    
    for i in free:
        t3 = timedelta(hours=int(i[0].split(":")[0]), minutes=int(i[0].split(":")[1]))
        t4 = timedelta(hours=int(i[1].split(":")[0]), minutes=int(i[1].split(":")[1]))
        # print((t1-t3).days)
        # print(t3-t1)
        # print(t2,t4)
        if (t1-t3).days >= 0 and (t4-t2).days >= 0:
            flag = flag+1
    
    return flag

free = []
for x in intervals:
    arr = x[0].split("-")
    free.append(arr)

final = []
for interval in ints:
    free_people = check_free(interval,free)
    # print(free_people)
    if free_people >= 2:
        final.append(interval)

print(final)
        

    
