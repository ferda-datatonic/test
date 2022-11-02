intervals = [[1,4],[4,5]]


#it might make sense to go through the array first
#and find the largest interval, first

#we can keep going through the array and finding
#the largest interval, merging all values that exist
#within the scope of this parent interval, taking its min and
#max values, create a new array with the result
#continue for the remaining elements

dummy = intervals.copy()
def custom_sort(val):
    return val[0]
res = []
while dummy != []:
    largest = 0
    index = 0
    for idx,i in enumerate(dummy):
        interval = abs(dummy[idx][0]-dummy[idx][1])
        if interval>largest:
            largest = interval
            index = idx
    temp = []
    curr = dummy.pop(index)
    temp.append(curr)
    l = 0
    while l <= len(dummy)-1 and dummy != []:
        if (dummy[l][0] >= curr[0] and dummy[l][0]<=curr[1]) or (dummy[l][1]<=curr[1] and dummy[l][1]>=curr[0]):
            temp.append(dummy[l])
            dummy.pop(l)
        else:
            l+=1   

    loc_min = 3497587
    loc_max = -4938595
    for results in temp:
        if results[0]<loc_min:
            loc_min = results[0]
        if results[1]>loc_max:
            loc_max = results[1]
    res.append([loc_min,loc_max])

print(res)