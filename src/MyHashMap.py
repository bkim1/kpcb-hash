"""
* HashMap implementation for KPCB Engineering Fellows Program
* Uses 
"""


class MyHashMap:
    def __init__(self, size=11):
        """
        * Initializes new HashMap with a fixed size
        """
        # Initialize Instance Variables
        self._num_elements = 0
        # Adjust fixed size for better load balance at max
        # Try to reach "max" size at 0.75 load factor
        size = int(size * 1.25)
        self._keys = ["" for i in range(size)]
        self._data = [None for i in range(size)]
        self._max_size = size

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
                return True

            elif index == 0 and self._keys[0] is not None \
                            and self._keys[0] != "" and key is None:
                return False

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
                # Find new index using linear probing
                index = self.find_key(key)
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
                # Find new index using linear probing
                index = self.find_key(key)
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
    
    def get_index(self, key, add=0):
        """
        * Helper method to get correct index for bucket
        * Uses python's default hash for strings 
        * Uses linear probing to find an open spot if collision occurs

        :param key: Key for HashMap 
        :return int: Returns index for bucket according to key and max_size
        """
        if key is None:
            return 0
        elif isinstance(key, str):
            return (hash(key) + add) % self._max_size
        
        raise ValueError("Expected: str Got: %s instead" % str(type(key)))

    def find_space(self, key):
        """
        * Helper method to find a new open space 
        * Calls get_index() method until an open space is found

        :param key: Key used to determine index in HashMap
        :return: Returns the index of an open spot or -1 if HashMap is full
        """
        for i in range(self._max_size):
            index = self.get_index(key, i)

            if self._keys[index] == "" or self._keys[index] == key:
                return index
        return -1

    def find_key(self, key):
        """
        * Helper method to find a key in HashMap if collision has occurred 
        * Calls get_index() method until the key is found

        :param key: Key used to determine index in HashMap
        :return: Returns the index of the key or -1 if not found
        """
        for i in range(self._max_size):
            index = self.get_index(key, i)

            if self._keys[index] == key:
                return index
        return -1

    def __len__(self):
        return self._num_elements

    def __repr__(self):
        rep = "{"
        if self._keys[0] is None and self._data[0] is not None:
            rep += " : %s" % self._data[0]
        elif self._keys[0] is None and self._data[0] is None:
            rep += " : "
        elif self._keys is not None:
            rep += self._keys[0] + ": "
        else:
            rep += self._keys[0] + ": %s" % self._data[0]

        for key, value in zip(self._keys, self._data):
            if value is None:
                rep += ", %s: " % key
            else:
                rep += ", %s: %s" % (key, value)

        rep += "}"
        return rep