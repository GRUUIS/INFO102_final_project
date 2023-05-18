import unittest
from Block import Block

class TestBlock(unittest.TestCase):
    
    def test_moveDown(self):
        block = Block()
        self.assertEqual(block.y, 0)
        self.assertEqual(block.x, 0)
        block.moveDown()
        self.assertEqual(block.x, 1)
        self.assertEqual(block.y, 0)
        
    
        
        
if __name__ == '__main__':
    unittest.main()
