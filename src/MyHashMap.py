"""
* HashMap implementation for KPCB Engineering Fellows Program
* Uses 
"""
# from src.MyLinkedList import LList, MyNode


class MyHashMap:
    def __init__(self, size=11):
        """
        * Initializes new HashMap with a fixed size
        """
        # Initialize Instance Variables
        self._num_elements = 0
        self._keys = ["" for i in range(size)]
        self._data = [None for i in range(size)]
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
            if index == 0 and self._keys[0] is None:
                self._data[0] = value
                return true

            elif self._keys[index] == "":
                self._keys[index] = key
                self._data[index] = value
                self._num_elements += 1
                return True
            
            else:
                if self._keys[index] == key:
                    self._data[index] = value
                    return True
                
                # ----- Collision has occurred ----- #
                index = self.find_space(key)
                if index == -1:
                    raise MemoryError("HashMap is full")
                elif self._keys[index] == key:
                    self._data[index] = value
                    return True
                else:
                    self._keys[index] = key
                    self._data[index] = value
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
            # Check for None 'key'
            if index == 0 and self._keys[0] is None:
                return self._data[0]
            
            # ----- Collision has occurred ----- #
            if self._keys[index] == "" or self._keys[index] != key:
                # Find new index using quadratic probing
                index = self.quad_search(key)
                if index == -1:
                    raise KeyError("Key not found")

            return self._data[index]

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
            # ------ Collision has occurred ------ #
            if self._keys[index] is not None and \
               (self._keys[index] == "" or \
               self._keys[index] != key):
                # Find new index using quadratic probing
                index = self.quad_search(key)
                if index == -1:
                    raise KeyError("Key not found")

            data = self._data[index]
            self._keys[index] = ""
            self._data[index] = None
            self._num_elements -= 1
            return data

    def load(self):
        """
        * Finds the load factor of current tree

        :return float: Returns load factor of current HashMap
        """
        return self._num_elements / self._max_size
    
    def get_index(self, key, quad=0):
        """
        * Helper method to get correct index for bucket
        * Uses python's default hash for strings 

        :param key: Key for HashMap 
        :return int: Returns index for bucket according to key and max_size
        """
        if key is None:
            return 0
        elif isinstance(key, str):
            return (hash(key) + quad*quad) % self._max_size
        
        raise ValueError("Expected: str Got: %s instead" % str(type(key)))

    def find_space(self, key):
        for i in range(self._max_size):
            index = self.get_index(key, i)
            print(index)

            if self._keys[index] == "" or self._keys[index] == key:
                return index
        return -1

    def quad_search(self, key):
        for i in range(self._max_size):
            index = self.get_index(key, i)

            if self._keys[index] != "" and self._keys[index] == key:
                return index
        return -1