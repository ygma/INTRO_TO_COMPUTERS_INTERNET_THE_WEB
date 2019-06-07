import unittest

def check(number):
    return 'even' if number % 2 == 0 else 'odd'

class MyTest(unittest.TestCase):
    def test(self):        
        self.assertEqual('even', check(4))
        self.assertEqual('even', check(0))
        self.assertEqual('odd', check(3))
        self.assertEqual('odd', check(-3))

if __name__ == '__main__':
    unittest.main()

    
