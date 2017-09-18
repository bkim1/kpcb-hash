import unittest
from src.MyHashMap import MyHashMap

class TestHashMap(unittest.TestCase):
    def test_set_and_get(self):
        hmap = MyHashMap()

        hmap.set("test", 10)
        hmap.set("hello", 25)
        hmap.set("watsup", 50)

        self.assertTrue(hmap.get("test") == 10)

    def test_get(self):
        hmap = MyHashMap()

        with self.assertRaises(KeyError):
            hmap.get("hi")


if __name__ == "__main__":
    unittest.main()