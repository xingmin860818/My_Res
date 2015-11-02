#测试sales.py的商品定价
import unittest
from sales import goods_price
class Test_price(unittest.TestCase):
        def test_prices(self):
                d = goods_price(a=1000,b=900,c=30000)
                self.assertEquals(d['a'],'640.00')
                self.assertEquals(d['b'],'576.00')
                self.assertEquals(d['c'],'19200.00')
                self.assertTrue(isinstance(d,dict))
        def test_key_error(self):
                with self.assertRaises(TypeError):
                        goods_price(1000)
        def test_value_error(self):
                with self.assertRaises(TypeError):
                        goods_price(b='1000')

if __name__=='__main__':
        unittest.main()
