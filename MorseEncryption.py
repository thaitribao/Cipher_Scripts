import sys
"""
This program encodes a file using 
Morse Code. Result is stored in 
a separate file 
"""

#Alphabet
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
			'U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
#MORSE_CODE table
MORSE_CODE = ["o-","-ooo","-o-o","-oo","o","oo-o","--o",
			"oooo","oo","o---","-o-","o-oo","--","-o","---",
			"o--o","--o-","o-o","ooo","-","oo-","ooo-","o--",
			"-oo-","-o--","--oo","-----","o----","oo---","ooo--",
			"oooo-","ooooo","-oooo","--ooo","---oo","----o"]

def morse_encrypt(input_string):
	result = ""
	input_string = input_string.upper()
	for char in input_string:
		if char in ALPHABET:
			number = ALPHABET.index(char)
			result = result + MORSE_CODE[number] + '/'
		else: 
			result = result + char + '/'
	return result


def main():
	
	#Get arguments in variables
	script,source,destination = sys.argv
	#file operations
	source_file = open(source)
	destination_file = open(destination,"w+")
	
	#operate line by line
	for line in source_file:
		encoded_line = morse_encrypt(line)
		destination_file.write(encoded_line)
		print (encoded_line)

	source_file.close()
	destination_file.close()

if __name__ == '__main__':
    main()

