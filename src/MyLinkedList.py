"""
* Linked List implementation for HashMap
"""

class LList:
    def __init__(self, node):
        """
        :param node: MyNode object within the linked list
        """
        if not isinstance(node, MyNode) and node is not None:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(node)))
        head = node
        current = head

    def delete(self, node):
        pass

    @property
    def head(self):
        return self.head

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
        elif n is not None or not isinstance(n, MyNode):
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(n)))

        key = k
        value = v
        next_node = n

    @property
    def key(self):
        return self.key

    @property.setter
    def key(self, k):
        if isinstance(k, str):
            self.key = k
        else:
            raise ValueError("Expected: str Got: %s" % str(type(k)))

    @property
    def value(self):
        return self.value

    @property.setter
    def value(self, v):
        self.value = v

    @property
    def next_node(self):
        return self.next_node

    @property.setter
    def next_node(self, n):
        if n is None or isinstance(n, MyNode):
            self.next_node = n
        else:
            raise ValueError("Expected: MyNode obj Got: %s" % str(type(n)))

    def __eq__(self, other):
        return self.key == other.key and \
               self.value == other.value and \
               self.next_node == other.next_node
    
    def __ne__(self, other):
        return not self == other

