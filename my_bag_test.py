#!/us/bin/env python
import unittest
from mybag import BackPack

class TestMybag(unittest.TestCase):
	def test_init(self):
		bag = BackPack()
		bag.add_stuff('apple',4,10)
		self.assertEquals(bag.show_stuffs(),{'apple':[4,40]})
		self.assertTrue(isinstance,(bag,dict))
	def test_get_stuff(self):
		bag = BackPack()
		bag.add_stuff('apple',4,10)
		bag.get_stuff('apple',2)
		self.assertEquals(bag.show_stuffs(),{'apple':[2,20]})
	def test_valueerror(self):
		bag = BackPack()
		with self.assertRaises(TypeError):
			bag.add_stuff('apple','4',10)
			bag.add_stuff('apple',4,'10')
			bag.get_stuff('apple','3')



if __name__=='__main__':
	unittest.main()
