class Node(object):
    def __init__(self, prev=None, next=None, key=None, value=None):
        self.prev, self.next, self.key, self.value = prev, next, key, value


class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.prev, node.next = node, node
        self.rootnode = node

    def headnode(self):
        return self.rootnode.next

    def tailnode(self):
        return self.rootnode.prev

    def remove(self, node):
        if node is self.rootnode:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def append(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.next = self.rootnode
        self.rootnode.prev = node


class LRUCache(object):
    def __init__(self,maxsize=16):
        self.maxsize = maxsize 
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self,func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:
                self.access.remove(cachenode)
                self.access.append(cachenode)
                return cachenode.value
            else:
                value = func(n)
                if not self.isfull:
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode,self.access.rootnode,n,value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                    self.isfull = len(self.cache) >= self.maxsize
                    return value 
                else:
                    lru_node = self.access.headnode()
                    del self.cache[lru_node.key]
                    self.access.remove(lru_node)
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode,self.access.rootnode,n,value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                return value 
        return wrapper




@LRUCache()     
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(1,35):
    print(fib(i))