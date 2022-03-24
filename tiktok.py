def inversion(arr):
    delete_duplicate = {}
    ans = 0
    for i in range(len(arr)):
        # cur is the second number
        cur = arr[i]
        # filter number have already calculated, because when an number have already shown before cur number, it has already count the numbers after cur number  
        if delete_duplicate.get(cur) == None:
            # count nums left to the cur number and bigger than cur number
            count_left = len(set([x for x in arr[:i] if x > cur]))
            # count nums right to the cur number and smaller than cur number
            count_right = len(set([x for x in arr[i:] if x < cur]))
            ans += count_left * count_right
            delete_duplicate[cur] = True
    return ans
