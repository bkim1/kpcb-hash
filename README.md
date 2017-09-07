HashMap implementation for KPCB Engineering Fellows Program

Written using Python v3.6.2


Methods Required:

* constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
* boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
* get(key): return the value associated with the given key, or null if no value is set.
* delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
* float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.