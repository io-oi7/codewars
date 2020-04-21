def getCount(inputStr):
	"""Return the number (count) of vowels in the given string.
	We will consider a, e, i, o, and u as vowels for this Kata.
	The input string will only consist of lower case letters and/or spaces.
	"""
	num_vowels = 0
	vowels = 'aeiou'
	for each_letter in inputStr:
		for each_vowel in vowels:
			if each_letter == each_vowel:
				num_vowels += 1
	return num_vowels

if __name__ == '__main__':
	print(getCount('Woot woot beeeeitch!'))