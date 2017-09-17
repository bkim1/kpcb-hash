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

    def add(self, key, value):
        if self.head is None:
            self.head = MyNode(key, value, None)
            self.current = self.head
            self.tail = self.head
            return True

        self.tail.next_node = MyNode(key, value, None)
        self.tail = self.tail.next_node
        return True

    def delete(self, key):
        curr = self.head
        prev = self.head
        while curr is not None:
            if curr.key == node.key:
                if curr == self.head:
                    self.head = None
                else:
                    prev.next_node = curr.next_node
                return curr.value
            prev = curr
            curr = curr.next_node
        return None

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        
        self._head = node

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

class MyNode:
    def __init__(self, k, v, n):
        if not isinstance(k, str):
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
        return self.key == other.key and \
               self.value == other.value and \
               self.next_node == other.next_node
    
    def __ne__(self, other):
        return not self == other


if __name__ == '__main__':
    llist = LList()
    i = 0
    for ch in 'abcde':
        llist.add(ch, i)
        i += 1

    for node in llist:
        print("Key: %s Value: %s" % (node.key, str(node.value)))
    
