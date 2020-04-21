def likes(names=[]):
	"""Names as a list of strings
	Returns names of people who liked the post, 
	folding at two people liked"""
	if names == []:
		return "No one likes this"
	elif len(names) == 1:
		return f"{names[0]} likes this"
	elif len(names) == 2:
		return f"{names[0]} and {names[1]} like this."
	elif len(names) == 3:
		return f"{names[0]}, {names[1]}, and {names[2]} like this"
	elif len(names) >= 4:
		return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
	else:
		print('invalid input')


if __name__ == '__main__':

	print(likes(names=['kalyb', 'kimberly', 'george', 'bo']))