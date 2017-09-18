"""
* HashMap implementation for KPCB Engineering Fellows Program
* Uses 
"""
from src.MyLinkedList import LList, MyNode


class MyHashMap:
    def __init__(self, size=10):
        """
        * Initializes new HashMap with a fixed size
        """
        # Initialize Instance Variables
        self._num_elements = 0
        self._buckets = [LList() for i in range(size)]
        self._max_size = size

    def __len__(self):
        return self._num_elements

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
            if self._num_elements == self._max_size:
                raise MemoryError("HashMap has reached max size. " \
                                + "Delete an item to make room.")
            bucket = self._buckets[index]
            if bucket.is_empty():
                bucket.add(key, value)
                self._num_elements += 1
                return True
        
            for node in bucket:
                if node.key == key:
                    node.value = value
                    return True
            
            bucket.add(key, value)
            self._num_elements += 1
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
            for node in self._buckets[index]:
                if node.key == key:
                    return node.value
            raise KeyError("Key not found")

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
            bucket = self._buckets[index]
            if bucket is None:
                return None

            try:
                value = bucket.delete(key)
            except KeyError:
                raise
            else:
                self._num_elements -= 1
                return value

    def load(self):
        """
        * Finds the load factor of current tree

        :return float: Returns load factor of current HashMap
        """
        return self._num_elements / self._max_size
    
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
            return hash(key) % (self._max_size - 1)
        
        raise ValueError("Expected: str Got: %s instead" % str(type(key)))
