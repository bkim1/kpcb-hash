"""
* HashMap implementation for KPCB Engineering Fellows Program
* Uses 
"""
from MyLinkedList import LList, MyNode


class MyHashMap:
    def __init__(self, size=100):
        """
        * Initializes new HashMap with a fixed size
        """
        # Initialize Instance Variables
        num_elements = 0
        buckets = [LList(None)] * size
        max_size = size

    def __len__(self):
        return self.num_elements

    def set(self, key, value):
        """
        * Stores given key:value pair in HashMap  

        :return bool: Returns success/failure of key:value being set
        """
        try:
            index = self.get_index(key)        
        except ValueError:
            return False
        else:
            if self.num_elements == self.max_size:
                # raise some error for maxed out HashMap
                pass
            bucket = self.buckets[index]
        
        for node in bucket:
            if node.key == key:
                node.value = value
                return True
            elif node.next_node is None:
                node.next_node = MyNode(key, value, None)
                self.num_elements += 1
                return True

    def get(self, key):
        """
        * Gets value found at given key

        :return value: Returns value found at key 
        """
        try:
            index = self.get_index(key)
        except ValueError:
            raise
        else:
            for node in self.buckets[index]:
                if node.key == key:
                    return node.value
            return None

    def delete(self, key):
        """
        * Deletes value found at given key

        :return value: Returns value if successfully deleted
        """
        try:
            index = self.get_index(key)
        except ValueError:
            raise
        else:
            bucket = self.buckets[index]
            if bucket is None:
                return None
            return bucket.delete(key)

    def load(self):
        """
        * Finds the load factor of current tree

        :return float: Returns load factor of current HashMap
        """
        return self.num_elements / self.max_size
    
    def get_index(self, key):
        """
        * Helper method to get correct index for bucket
        * Uses python's default hash for strings 

        :param key: Key for HashMap 
        :return int: Returns index for bucket according to key and max_size
        """
        if key is None:
            return 0
        elif isinstance(key, str):
            return hash(key) % self.max_size
        
        raise ValueError("Expected: str Got: %s instead" % str(type(key)))
