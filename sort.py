#coding:utf-8

# insert sort
def insert_sort(lst):
    for i in range(1,len(lst)):
        item = lst[i]
        j = i -1 
        while j >=0 and lst[j]>item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = item
    return lst

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print(ls)
print('insert sort')
print(insert_sort(ls))


def dubble_sort(lst):
    n = len(lst) -1 
    for i in range(n):
        for j in range(n):
            if lst[j+1] > lst[j]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
        j -= 1 
    return lst 

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print('dubble sort')
print(dubble_sort(ls))



def select_sort(lst):
    n  = len(lst)
    for i in range(n):
        for j in range(i,n):
            if lst[j]< lst[i]:
                lst[j],lst[i] = lst[i],lst[j]
    return lst

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print('select sort')
print(select_sort(ls))


# quick sort by 
def quick_sort(lst):
    if len(lst)<=1:
        return lst 
    return quick_sort([i for i in lst[1:] if i < lst[0]]) + lst[0:1] + \
        quick_sort([i for i in lst[1:] if i >= lst[0]])

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print('quick sort')
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

ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
qsort(ls,0,len(ls)-1)
print('quick sort')
print(ls)




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



ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print('merge sort')
print(merge_sort(ls))