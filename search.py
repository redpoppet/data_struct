def binary_search(lst,val):
    if len(lst) == 0:
        return 

    low,high = 0,len(lst) -1 
    while low <= high:
        mid = (high+low)//2
        if lst[mid] ==val:
            return mid
        elif lst[mid] <val:
            low = mid +1 
        else:
            high = mid -1 
    return low 



lst = [1,2,3,5,6,7]
print(binary_search(lst,5))