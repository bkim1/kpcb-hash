"""
* Linked List implementation for HashMap
"""

class LList:
    def __init__(self, node=None):
        """
        :param node: MyNode object within the linked list
        """
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        
        self._head = node
        self._current = self.head
        self._tail = self.head
        if node is None:
            self._num_elements = 0
        else:
            self._num_elements = 1

    def add(self, key, value):
        if self.head is None:
            self.head = MyNode(key, value, None)
            self.current = self.head
            self.tail = self.head 
        else:
            self.tail.next_node = MyNode(key, value, None)
            self.tail = self.tail.next_node
        
        self._num_elements += 1
        return True

    def delete(self, key):
        curr = self.head
        prev = self.head
        while curr is not None:
            if curr.key == key:
                if curr == self.head:
                    self.head = None
                else:
                    prev.next_node = curr.next_node

                self._num_elements -= 1
                return curr.value
            prev = curr
            curr = curr.next_node
        
        raise KeyError("Key not found within list")

    def is_empty(self):
        return self.head is None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        
        self._head = node
    
    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        
        self._tail = node
    
    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, node):
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        
        self._current = node

    def __len__(self):
        return self._num_elements

    def __iter__(self):
        return self

    def __next__(self):
        node = self.current
        if node is None:
            self.current = self.head
            raise StopIteration
        else:
            self.current = node.next_node
        return node

    def __repr__(self):
        if self.is_empty():
            return "[]"
        items = "["
        node = self.head
        while node is not None:
            if node.next_node is None:
                items += str(node) + "]"
            else:
                items += str(node) + ", "
            
            node = node.next_node

        return items


class MyNode:
    def __init__(self, k, v, n):
        if not isinstance(k, str) and k is not None:
            raise ValueError("Expected: str Got: %s" % str(type(k)))
        elif n is not None and not isinstance(n, MyNode):
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(n)))

        self._key = k
        self._value = v
        self._next_node = n

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        if isinstance(k, str):
            self._key = k
        else:
            raise ValueError("Expected: str Got: %s" % str(type(k)))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, n):
        if n is None or isinstance(n, MyNode):
            self._next_node = n
        else:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(n)))

    def __eq__(self, other):
        if self.next_node is None and other.next_node is None:
            return self.key == other.key and \
                   self.value == other.value
        elif self.next_node is None or other.next_node is None:
            return False
        else:
            return self.key == other.key and \
                   self.value == other.value and \
                   self.next_node == other.next_node
    
    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "'%s': %s" % (self.key, self.value)
