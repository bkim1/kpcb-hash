import unittest
import time
from src.MyHashMap import MyHashMap

class TestHashMap(unittest.TestCase):
    def test_speed(self):
        
        hmap = MyHashMap(size=50)
        t0 = time.time()
        for i in range(40):
            hmap.set("t" + str(i), i)

        hmap.get("t2")
        hmap.get("t3")
        t1 = time.time()

        pydict = {}
        t2 = time.time()
        for i in range(40):
            pydict["t" + str(i)] = i
        
        pydict.get("t2")
        pydict.get("t3")
        t3 = time.time()

        print(hmap._buckets)
        print(pydict)
        print("MyHashMap: %f" % (t1 - t0))
        print("Dictionary: %f" % (t3 - t2))


    def test_get(self):
        hmap = MyHashMap()

        with self.assertRaises(KeyError):
            hmap.get("hi")
    
    def test_get_2(self):
        hmap = MyHashMap()

        hmap.set("test", 10)
        hmap.set("hello", 25)
        hmap.set("watsup", 50)

        self.assertTrue(hmap.get("test") == 10)
    
    def test_get_3(self):
        hmap = MyHashMap()

        with self.assertRaises(ValueError):
            hmap.get(10)

    def test_set(self):
        hmap = MyHashMap()
        hmap.set("test", 10)

        self.assertEqual(len(hmap), 1)

    def test_set_2(self):
        hmap = MyHashMap()

        with self.assertRaises(MemoryError):
            for i in range(11):
                hmap.set("t" + str(i), i)
    
    def test_set_3(self):
        hmap = MyHashMap()

        self.assertFalse(hmap.set(10, 10))    

    def test_set_4(self):
        hmap = MyHashMap()

        hmap.set(None, 10)
        self.assertFalse(hmap._buckets[0].is_empty())

    def test_delete(self):
        hmap = MyHashMap()

        for i in range(8):
            hmap.set("t" + str(i), i)
        
        self.assertEqual(hmap.delete("t2"), 2)

    def test_delete_2(self):
        hmap = MyHashMap()

        for i in range(8):
            hmap.set("t" + str(i), i)
        
        hmap.delete("t2")
        self.assertEqual(len(hmap), 7)

    def test_delete_3(self):
        hmap = MyHashMap()

        with self.assertRaises(ValueError):
            hmap.delete(10)

    def test_delete_4(self):
        hmap = MyHashMap()

        self.assertIsNone(hmap.delete("test"))

    def test_load(self):
        hmap = MyHashMap()

        hmap.set("test", 10)
        self.assertEqual(hmap.load(), 0.1)

if __name__ == "__main__":
    unittest.main()