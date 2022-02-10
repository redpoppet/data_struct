import ctypes

class Array:
    def __init__(self,size):
        assert size>0,'array size must be >0'
        self._size = size 
        PyArrayType = ctypes.py_object * size 
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __setitem__(self,index,value):
        assert index>= 0 and index < len(self),'out of range'
        self._elements[index] = value 


    def __getitem__(self,index):
        assert index>=0 and index < len(self),'out of range'
        return self._elements[index]
    
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i] = value 
    
    def __iter__(self):
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    def __init__(self,items):
        self._items = items
        self._idx = 0 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self._idx < len(self._items):
            val = self._items[self._idx]
            self._idx += 1 
            return val
        else:
            raise StopIteration




array = Array(3)
array[1] = 2
# print(array[1])
for item in array:
    print(item)



class Array2D:
    def __init__(self,numrows,numcols):
        self._the_rows = Array(numrows)
        for i in range(numrows):
            self._the_rows[i] =  Array(numcols)

    def numRows(self):
        return len(slef._the_rows)