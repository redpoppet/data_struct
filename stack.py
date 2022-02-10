aaa = [1,23,5]



from collections import deque 

queue = deque([1,2,3,5])

queue.append(9)
for item in queue:
    print(item,sep=',')


