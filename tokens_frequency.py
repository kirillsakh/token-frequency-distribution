def calculate_frequency(input_file, patterns, encoding_type=None, output_file=None):
	"""'calculate_frequency(input_file, patterns, encoding_type, output_file)':
	   returns dictionary that contains 
	   frequency of tokens from the given file

	   input_file ... plain text file in that encoding	   
	   patterns ... list of strings to find
	   encoding_type ... character encoding	(utf-8 if not specified)   
	   output_file ... name of a file to write the output to

	"""
	if encoding_type == None: # default encoding
		encoding_type = "utf-8"
	
	if output_file == None: # default output file name
		output_file = "output.txt"

	try:#better safe than sorry
		with open(input_file, encoding=encoding_type) as file:
			lines = file.readlines() # read lines from file to list
	except FileNotFoundError:
		print("File not accessible")

	result = {} # initialize dictionary to store frequency counts

	for line in lines: # process input line by line
		token = '' # initialize token object
		for char in line: # iterate over all characters in line
			if char != ' ' and char != '\n': # tokens are set of characters separated by white-spaces or newlines
				token += char # add character to the token
			else:
				if len(token) != 0: # if token,
					for string in patterns: # check string patterns
						if string in token: # if match,
							if not token in result:
								result[token] = 1 # if new match, count equals one
							else:
								result[token] += 1 # else, increment match count
							break # no need to continue; avoid duplicity
					token = '' # empty token object
	
	with open(output_file, "a") as file:
		for key in result:
			file.write(f"{key} {result[key]}\n")
		file.write(f"{'-'*10}\n")

	return result

def test_function():
	print("Testing", calculate_frequency.__doc__)
	
	test_dictionary = {
	"awe":    1,
	"pa,":     1,
	"pat":    2,
	"pawes.": 1,
	"we" :    2
	}

	output_dictionary = calculate_frequency('test.txt', ['pa', 'we'])
	
	for key in sorted(output_dictionary): # print results
		print(f"{key}: {output_dictionary[key]}")
	
	print("\nTestcase #1", end=' ')
	for key in test_dictionary:
		if not key in output_dictionary or \
		test_dictionary[key] != output_dictionary[key]:
			print("Fail")
			return
	print("OK")

if __name__ == '__main__':
	test_function()

# Bonus: linux shell solution
# cat test.txt | tr ' ' '\n' | awk '/pa|we/' | sort | uniq -c > output.txt