import unittest
from sales import set_price

class Test_price(unittest.TestCase):
        def test_kv(self):
                d = set_price(a=10,b=50)
                self.assertEquals(d['a'],10*0.9)
                self.assertEquals(d['b'],50*0.9)
                self.assertTrue(isinstance(d,dict))
        def test_error(self):
                with self.assertRaises(TypeError):
                        set_price(a='10')
                        set_price('a')

if __name__ == '__main__':
        unittest.main()
