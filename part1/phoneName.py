import sys
import re
import collections

def stdPhone(num):
	"""
	input: str, num is the phone number
	output: str, num that is standardized as (999)000-1234
	"""
	if num == "":
		return ''
	number = re.split("[()-.]", num)
	number = ''.join(number)
	if len(number) == 10:
		return '('+number[:3]+')'+number[3:6]+'-' + number[6:]
	else:
		return number[:3]+'-'+number[3:]


if __name__ == '__main__':
	f = open(sys.argv[1], 'r')
	# sys.argv[1] must be the file name of the input file.
	dis = f.readlines();
	f.close

	numPerson = collections.defaultdict(list) # a dictionary to hold the phone number and the name

	for i in dis:
		content = re.split("[\t\n]", i)
		phoneNo = stdPhone(content[1])
		numPerson[phoneNo].append(content[0])

	with open(sys.argv[2], 'w') as file:
		for phone, name in numPerson.items():
			file.write(phone+'\t'+','.join(name)+'\n')




		



