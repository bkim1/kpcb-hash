HashMap implementation for KPCB Engineering Fellows Program

Written using Python v3.6.2

## Dependencies needed to run:
* Python v3.6

## How to use MyHashMap
* Import `MyHashMap.py`
* Initialize a new MyHashMap with a fixed size

Example:
```python
myhashmap = MyHashMap(size=100)
```
* Use as needed

## How to run unit tests:
1. Open terminal to root directory 
2. Run `python3 -m tests.test_myhashmap`


## HashMap Methods:

* constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
* boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
* get(key): return the value associated with the given key, or null if no value is set.
* delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
* float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the data structure is fixed, this should never be greater than 1.