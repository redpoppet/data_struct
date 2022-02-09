
# quick sort by 
def quick_sort(lst):
    if len(lst)<=1:
        return lst 
    return quick_sort([i for i in lst[1:] if i < lst[0]]) + lst[0:1] + \
        quick_sort([i for i in lst[1:] if i >= lst[0]])

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print(ls)
print(quick_sort(ls))



def qsort(lst,left,right):
    
    if left>=right:
        return 
    
    start,end = left,right 
    mid = lst[start]

    while start<end:
        while start<end and lst[end] >= mid:
            end -= 1   
        lst[start] = lst[end]
        while start<end and lst[start] < mid:
            start += 1 
        lst[end] = lst[start]

    lst[start] = mid
    qsort(lst,start+1,right)
    qsort(lst,left,start-1)

lst = [2,2,3,4,7,9,3,2,3,1]
qsort(lst,0,len(lst)-1)
print(lst)




# merge sort

def merge_sort(lst):
    if len(lst)<= 1:
        return lst

   
    mid = len(lst) // 2
    left_lst = merge_sort(lst[:mid])
    right_lst = merge_sort(lst[mid:])
    i= j = 0 
    res = []  # 存放结果
    while i<len(left_lst) and j <len(right_lst):
        if left_lst[i]<=right_lst[j]:
            res.append(left_lst[i])
            i+= 1
        else:
            res.append(right_lst[j])
            j += 1
    res.extend(left_lst[i:])
    res.extend(right_lst[j:])
    return res



lst = [2,2,3,4,7,9,3,2,3,1]
print(merge_sort(lst))