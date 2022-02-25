from datetime import datetime, timedelta

intervals = [["12:30-18:00"], ["12:15-19:00","07:00-12:00"], ["00:00-18:00"]]

available_times = []


def check_availablity(intervals,hour,minute):
    flag = 0
    time_frame = str(hour)+str(minute)
    if hour < 10 and len(time_frame)<3:
        time_frame = time_frame+"0"
    elif hour >= 10 and len(time_frame) <4:
        time_frame = time_frame+"0"
  
    time_frame = int(time_frame)
    
    t1 = time_frame
    t2 = (time_frame+15)
    
    
    for i in intervals:
        available = False
        for t in i:
            t = t.split("-")
            
            t3 = int(t[0].split(":")[0]+t[0].split(":")[1])
            t4 = int(t[1].split(":")[0]+t[1].split(":")[1])
            
            # if hour == 8:
            #     print(t1,t2,t3,t4)
            
            if (t3-t1) > 0 and (t4-t2) > 0:
                available = True
            elif (t3-t1) < 0 and (t4-t2) < 0:
                available = True
            else:
                available = False
                break
        
        
        if available == True:
            flag = flag+1
    
    return flag
            
            

for hour in range(0,24):
    if hour == 24:
        minute_range = 15
    else:
        minute_range = 59
    for minute in range(0,minute_range,15):
        available_employees = check_availablity(intervals,hour,minute)
        if available_employees >=2:
            
            h = f'{hour:02d}'
            m = f'{minute:02d}'
            if minute == 45:
                hour = hour+1
                minute = 0
            else:
                minute = minute+15
            
            h_2 = f'{hour:02d}'
            m_2 = f'{minute:02d}'
                
            available_times.append(h+":"+m+"-"+h_2+":"+m_2)
    
print(available_times)
            
        
