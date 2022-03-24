def droppedRequests(requestTime):
    # Write your code here
    dropped = 0
#       to keep track of already dropped we will use dictionary
    prevDrop = {} 

    for i in range(len(requestTime)):
        if i > 2 and requestTime[i] == requestTime[i-3]:
            if requestTime[i] not in prevDrop or prevDrop[requestTime[i]] != i:
                prevDrop[requestTime[i]] = i
                dropped += 1

        elif i > 19 and requestTime[i] - requestTime[i-20] < 10:
            if requestTime[i] not in prevDrop or prevDrop[requestTime[i]] != i:
                prevDrop[requestTime[i]] = i
                dropped += 1

        elif i > 59 and requestTime[i] - requestTime[i-60] < 60:
            if requestTime[i] not in prevDrop or prevDrop[requestTime[i]] != i:
                prevDrop[requestTime[i]] = i
                dropped += 1

    return dropped
