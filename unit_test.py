import unittest
import calc
  
class SimpleTest(unittest.TestCase):
  
    def test(self):
        # if calc.calculate(5, 6, '-') == -2:
        #     return True
        # else:
        #     return False
        assert calc.calculate(5, 6, '-') == -1
  
if __name__ == '__main__':
    unittest.main()