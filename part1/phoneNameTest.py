import unittest
from phoneName import PhonePerson

class TestPhoneName(unittest.TestCase):
	def setUp(self):
		self.contacts = []
		self.contacts.append(PhonePerson("1112334444", "John"))
		self.contacts.append(PhonePerson("2331234", "Paul Tophat"))
		self.contacts.append(PhonePerson("(900)2341234", "Zoe Brandy"))
		self.contacts.append(PhonePerson("900234-1234", "Sophie"))
		self.contacts.append(PhonePerson("233-1234", "Jerry Strong"))
		self.contacts.append(PhonePerson("111.233.4444", "Brad Miller"))
		self.contacts.extend([PhonePerson("(999)234.2233", "Karl"), \
			PhonePerson("999.234-2234", "Marry"),\
			PhonePerson("999-234.2233", "Justin Given")])

	def testStdPhone0(self):
		self.assertIsNone(self.contacts[0].stdNum)
		self.contacts[0].stdPhone()
		self.assertEqual(self.contacts[0].stdNum, "(111)233-4444")

	def testStdPhone1(self):
		self.contacts[1].stdPhone()
		self.assertEqual(self.contacts[1].stdNum, "233-1234")

	def testStdPhone2(self):
		self.contacts[2].stdPhone()
		self.contacts[3].stdPhone()
		self.assertEqual(self.contacts[2].stdNum, self.contacts[3].stdNum)
		self.assertNotEqual(self.contacts[2].num, self.contacts[3].num)

	def testStdPhone3(self):
		self.contacts[4].stdPhone()
		self.contacts[1].stdPhone()
		self.assertEqual(self.contacts[4].stdNum, self.contacts[1].stdNum)
		self.assertNotEqual(self.contacts[4].num, self.contacts[1].num)
		self.assertNotEqual(self.contacts[4].name, self.contacts[1].name)

	def testStdPhone4(self):
		self.contacts[5].stdPhone()
		self.contacts[0].stdPhone()
		self.assertEqual(self.contacts[0].stdNum, self.contacts[5].stdNum)
		self.assertNotEqual(self.contacts[0].num, self.contacts[5].num)
		self.assertNotEqual(self.contacts[0].name, self.contacts[5].name)

	def testStdPhone5(self):
		for i in range(6,9):
			self.contacts[i].stdPhone()
		self.assertEqual(self.contacts[6].stdNum, self.contacts[8].stdNum)
		self.assertNotEqual(self.contacts[7].stdNum, self.contacts[8].stdNum)
		self.assertNotEqual(self.contacts[6].name, self.contacts[8].name)

	def testSetNumPerson1(self):
		for i in range(5):
			self.contacts[i].stdPhone()
			self.contacts[i].setnumPerson()
		dicPhonePer = PhonePerson.getNumPerson()
		expected = {'(111)233-4444':['John'], '233-1234':['Paul Tophat', 'Jerry Strong'],\
		 '(900)234-1234':['Zoe Brandy', 'Sophie']}
		self.assertDictEqual(dicPhonePer, expected)

	def testSetNumPerson2(self):
		for i in range(6,9):
			self.contacts[i].stdPhone()
			self.contacts[i].setnumPerson()
		dicPhonePer = PhonePerson.getNumPerson()
		expected = {'(111)233-4444':['John'], '233-1234':['Paul Tophat', 'Jerry Strong'],\
		 '(900)234-1234':['Zoe Brandy', 'Sophie'], '(999)234-2233':['Karl', 'Justin Given'],'(999)234-2234':['Marry']}
		for key in expected.keys():
			self.assertEqual(dicPhonePer[key], expected[key])
		self.assertDictEqual(dicPhonePer, expected)

if __name__ == '__main__':
	unittest.main()