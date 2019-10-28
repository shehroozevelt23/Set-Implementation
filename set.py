## Last version: 17 May 2019

## A class implementing contiguous memory

class Contiguous:
    """    
    Fields: _items is a list of items
            _size is number of items that can be stored
    """

    ## Contiguous(s) produces contiguous memory of size s
    ##     and initializes all entries to None.
    ## __init__: Int -> Contiguous
    ## Requires: s is positive
    def __init__(self, s):
        self._items = []
        self._size = s
        self._first = 0
        for index in range(self._size):
            self._items.append(None)

    ## self.string_access(index) produces a string version of the value stored
    ##  at index
    ## contents: Nat -> Str
    def string_access(self, index):
        if self.access(index) == None:
            return "None"
        else:
            return str(self.access(index))        

    ## repr(self) produces a string with the sequence of values.
    ## __repr__: Contiguous -> Str
    def __repr__(self):
        if self._first == 0:
            return "( )"
        to_return = "("
        for index in range(self._first - 1):
            to_return = to_return + self.string_access(index) + ","
        return to_return + self.string_access(self._first - 1) +")"

    ## self.size() produces the size of self.
    ## size: Contiguous -> Int
    def __len__(self):
        return self._first

    ## self == other produces True if self and other have the same
    ##     size and store the same values at each index.
    ## __eq__: Contiguous Contiguous -> Bool
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for pos in range(len(self)):
                if self.access(pos) != other.access(pos):
                    return False
            return True

    ## self != other produces True if self and other differ in size
    ##     or values at at least one index.
    ## __ne__: Contiguous Contiguous -> Bool
    def __ne__(self, other):
        if len(self) != len(other):
            return True
        else:
            for pos in range(len(self)):
                if self.access(pos) != other.access(pos):
                    return True
            return False  

    ## self.store(index, value) stores value at the given index if there is 
    ##    an empty slot and produces True
    ##    otherwise, produces False
    ## Effects: Mutates self by storing value at the given index.
    ## store: Contiguous Int Any -> Bool
    ## Requires: 0 <= index < self._size
    def store(self, value):
        if 0 <= self._first and self._first < self._size: 
            self._items[self._first] = value
            self._first += 1
            return True
        return False
            

    ## for element in self:
    ##       body
    ## loops over self. Runs body for each element in self
    ## __iter__(self): Set -> 
    def __iter__(self):
        return iter(self._items[0:self._first])


LIMIT = 20

class Set:
    """
    Fields: _items contains the objects stored in the set
    """
    
    ## Set() produces an empty set
    ## __init__: -> Set
    def __init__(self):
        self._items = Contiguous(LIMIT)
    
    
    ## for element in self:
    ##       body
    ## loops over self. Runs body for each element in self
    ## __iter__(self): Set -> 
    def __iter__(self):
        return iter(self._items)    
    
    
    ## item in self produces true if item exists in self, False otherwise
    ## __contains__: Set Any -> Boolean
    def __contains__(self, item):
        for elem in self:
            if elem == item:
                return True
        return False
    
    
    ## self.add(item) adds item into self, produces True if the item is added,
    ##          otherwise False
    ## Effects: Mutates self to contain item
    ## add: Set Any -> Bool
    def add(self, item):
        if item in self:
            return False
        return self._items.store(item)
        

    
    ## len(self) produces the number of items stored in self
    ## __len__: Set -> Nat
    def __len__(self):
        return len(self._items)