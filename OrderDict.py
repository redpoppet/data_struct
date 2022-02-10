class OrderDict(dict):

    def __init__(*args,**kwds):
        if not args:
            raise TypeError("needs an argument")
        
        self = args[0]
        args = args[1:]
        if len(args)>1:
            raise TypeError('Expected at most 1 arguments')
        try:
            self.__root
        except AttributeError:
            self.__root = root = []
            root[:] = [root,root,None]
            self.__map = {}
        self.__update(*args,**kwds)

    
    def __delitem__(self, key,dict_delitem=dict.__delitem__):
        dict_delitem(self,key)
        link_prev,link_next,_ = self.__map.pop(key)
        link_prev[1] = link_next
        link_next[0] = link_prev
