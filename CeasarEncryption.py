from sys import argv
"""
This script encodeds a file using 
Ceasar cipher
"""
#Array holding alphabet letters
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

"""
#associate filename with the argument passed in
script, filename = argv

#txt = the file
txt = open(filename)


#read and encode each line
"""

"""
encodeCeasar: encode a string using Ceasar Cipher
Input: encoded_string: string to be encoded
	   offset: steps of Ceasar Cipher
Return: encoded string using Ceasar Cipher
"""
def encodeCeasar(encoded_string, off_set):
	result = ""
	encoded_string = encoded_string.upper()
	for encoded_char in encoded_string:
		if(encoded_char.isalpha()):
			char_index = ALPHABET.index(encoded_char)
			char_index = (char_index + off_set)%26
			encoded_char = ALPHABET[char_index]
		else: 
			pass
		result += encoded_char
	return result

def main():
	
	#Get arguments in variables
	script,source,destination,first_key,second_key = argv
	first_key = first_key.upper()
	second_key = second_key.upper()
	#find offset
	offset = ALPHABET.index(second_key) - ALPHABET.index(first_key)
	#correct offset if needed
	if offset < 0:
		offset = 26 + offset
	#file operations
	source_file = open(source)
	destination_file = open(destination,"w+")
	
	#operate line by line
	for line in source_file:
		encoded_line = encodeCeasar(line, offset)
		destination_file.write(encoded_line)
		print (encoded_line)

	source_file.close()
	destination_file.close()

if __name__ == '__main__':
    main()

