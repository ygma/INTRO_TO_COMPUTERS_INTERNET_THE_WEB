import unittest

def cal_sum_fibo(n):
    if n == 1: return 1
    a, b = 1, 1
    sum = a + b
    for i in range(3, n + 1):
        c = a + b
        sum += c
        a, b = b,c
        
    return sum
    
class TestCase(unittest.TestCase):
    def test_should_return_sum_of_fibo(self):
        self.assertEqual(2, cal_sum_fibo(2))
        self.assertEqual(54, cal_sum_fibo(8))
        self.assertEqual(1, cal_sum_fibo(1))
        
if __name__ == '__main__': unittest.main()   
