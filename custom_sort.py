us_list =[1,2,3,4,5,6,7,8]

s_list = []

fl = 0
ans = 0
for i in range(0,len(us_list)):
    if us_list[i] % 2 == 0:
        if i != fl:
            us_list[i],us_list[fl] = us_list[fl],us_list[i]
            fl = fl+1
            ans = ans+1
        else:
            fl = fl+1


        
print(us_list,ans)
