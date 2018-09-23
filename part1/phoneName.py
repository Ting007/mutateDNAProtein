import sys
import re
import collections

class PhonePerson():
	"""docstring for PhoneNumber"""
	numPerson = collections.defaultdict(list) # a dictionary to hold the phone number and the name

	def __init__(self, number, name):
		"""
		constructor
		"""
		self.num = number
		self.name = name
		self.stdNum = None

	def stdPhone(self):
		"""
		self.num is the phone number from the input file
		num may and may not be standard
		set the self.stdNum as standardized as (999)000-1234
		if not with area code standardized as 123-2345
		"""
		if self.num == "":
			self.stdNum = ''
		number = re.split("[()-.]", self.num)
		number = ''.join(number)
		if len(number) == 10:
			self.stdNum = '('+number[:3]+')'+number[3:6]+'-' + number[6:]
		else:
			self.stdNum = number[:3]+'-'+number[3:]

	def setnumPerson(self):
		PhonePerson.numPerson[self.stdNum].append(self.name)

	def getNumPerson():
		return PhonePerson.numPerson


if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	# sys.argv[1] must be the file name of the input file.
	dis = f.readlines();
	f.close

	res = []

	for i in dis:
		content = re.split("[\t\n]", i)
		phone = content[1]
		name = content[0]
		res.append(PhonePerson(phone, name))

	for item in res:
		item.stdPhone()
		item.setnumPerson()

	Phonelist = PhonePerson.getNumPerson()

	with open(sys.argv[2], 'w') as file:
		for phone, name in Phonelist.items():
			file.write(phone+'\t'+','.join(name)+'\n')




		



