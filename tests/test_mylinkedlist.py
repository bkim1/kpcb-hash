import unittest
from src.MyLinkedList import MyNode, LList

class TestLList(unittest.TestCase):
    def test_add(self):
        llist = LList()
        i = 0
        for ch in 'abcde':
            llist.add(ch, i)
            i += 1

        self.assertEqual(5, len(llist))

    def test_delete(self):
        llist = LList()
        i = 0
        for ch in 'abcde':
            llist.add(ch, i)
            i += 1
        
        self.assertEqual(2, llist.delete("c"))
    
    def test_delete_2(self):
        llist = LList()
        i = 0
        for ch in 'abcde':
            llist.add(ch, i)
            i += 1
        
        with self.assertRaises(KeyError):
            llist.delete("bc")

    def test_delete_3(self):
        llist = LList()
        i = 0
        for ch in 'abcde':
            llist.add(ch, i)
            i += 1
        
        llist.delete("b")
        self.assertEqual(4, len(llist))

    def test_node_eq(self):
        n0 = MyNode("a", 10, None)
        n1 = MyNode("a", 10, None)

        self.assertTrue(n0 == n1)

    def test_node_ne(self):
        n0 = MyNode("a", 10, None)
        n1 = MyNode("a", 10, n0)

        self.assertTrue(n0 != n1)

if __name__ == "__main__":
    unittest.main()