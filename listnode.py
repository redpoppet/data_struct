class ListNode(object):
    def __init__(self,data,p=None):
        self.data = data 
        self.next = p 
    

class LinkList(object):
    def __init__(self,data):
        self.head = ListNode(data=None)
        self.tail = self.head
        self.size = 0

        if len(data)>0:
            p = self.head 
            for item in data:
                p.next = ListNode(item)
                p = p.next
                self.size += 1 


    def show(self,head=None):
        p = self.head if not head else head 
        if p == None:
            return [] 
        result = list()
        while p.next:
            result.append(p.next.data)
            p = p.next
        print(result)
        
    @property
    def is_empty(self):
        return self.head.next == None 

    @property
    def length(self):
        return self.size


    def append(self,data):
        if self.head.next:
            p = self.head
            while p.next:
                p = p.next
            p.next = ListNode(data)
        else:
            self.head.next = ListNode(data)
        
        self.size += 1 



    def insert(self,data,pos=None):
        if pos>self.length or pos< 0:
            raise Exception('wrong pos')
        
        if self.is_empty and pos != 1:
            raise Exception('wrong pos')
        

        if data and pos is None:
            p = self.head
            while p.next:
                p = p.next 
            p.next = ListNode(data)
        
        if data and pos>=0 and pos < self.length:
            p = self.head
            count = 0 
            while p.next and count< pos:
                count += 1
                p = p.next
            new_p = ListNode(data)
            new_p.next = p.next
            p.next = new_p

    def delete(self,pos):
        
        if pos>self.length or pos< 0:
            raise Exception('wrong pos')

        if self.is_empty and pos != 1:
            raise Exception('wrong pos')
        p = self.head
        count = 0 
        while p.next and count<pos:
            count += 1
            p = p.next 
        temp_p = p.next
        p.next = p.next.next
        del temp_p

    def reverse(self):
        if self.head.next==None:
            return self.head

        pre = None
        cur = self.head.next 

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        self.head.next = pre

    def findKthNode(self,k):
        pre=cur = self.head.next
        count = 0 
        while cur.next and count<k-1:
            count += 1
            cur = cur.next
        while cur.next:
            cur = cur.next
            pre = pre.next 

        return pre.data

    def deleteDuplicates(self):
        pre =  self.head
        cur = self.head.next
        while cur:
            if cur.data == pre.data:
                cur = cur.next
                pre.next = cur
               
            else:
                cur = cur.next
                pre = pre.next

        


class LinkListWidget(object):

    def merge(self,phead,qhead):
        if phead == None:
            # while qhead.next:
            #     print(qhead.next.data)
            #     qhead = qhead.next
            return qhead 
        if qhead == None:
            # while phead.next:
            #     print(phead.next.data)
            #     phead = phead.next
            return phead
        if phead.data<= qhead.data:
            phead.next = self.merge(phead.next, qhead)
            return phead
        else:
            qhead.next = self.merge(phead, qhead.next)
            return qhead

    
    def check_intersection(self,phead,qhead):
        p1,p2 = phead,qhead
        while p1 is not p2:
            p1 = qhead if not p1 else p1.next
            p2 = phead if not p2 else p2.next
        return p1 




if __name__ == '__main__':

    lst = LinkList([1,1,2,3,5,5,6,6,7,7])
    # lst1 = LinkList([1,2,3,5,6,7])
    # lst2 = LinkList([1,2,3,4,8,9,10])
    # lst.show()
    # lst.append(6)
    # lst.show()
    # lst.insert(3,0)
    # lst.show()
    # lst.delete(0)
    # lst.show()
    # lst.reverse()
    # lst.show()
    # print(lst.findKthNode(1))
    # head = LinkListWidget().merge(lst1.head.next, lst2.head.next) 
    # result = list()
    # while head:
    #     result.append(head.data)
    #     head = head.next
    
    lst.deleteDuplicates()
    lst.show()


                
