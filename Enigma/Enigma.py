"""
Enigma Cipher program
Encipher a text file using Enigma Cipher
Number of rotors can be specified
Rotors can be used in different positions

++Date created: 12/21/2016
++Author: Bao Thai - btt4530@g.rit.edu
"""
from RotorBox import ROTORS
from MirrorBox import MIRRORS
from sys import argv

#Array holding alphabet letters
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#print(ROTORS[1][ALPHABET.index("A")])
#print(MIRRORS[0][1])

"""
Find the input to a rotor that gives the specified output
Param: rotor: investigated rotor
	   shift: shift of said rotor (0-26)
	   output: output to find the input
Output: The input that gives the specified output (inverse function)
"""
def findInput(rotor,shift,output):
	current_rotor = rotor
	count = 0 
	while count < len(rotor):
		pos = (count + shift)%26 #which shift are being used 
		out_check = (count + rotor[pos])%26 #output of current count
		if out_check < 0: 
			out_check = 26 + out_check
		if out_check == output:
			return count
		count = count + 1


"""
Encode a line using Enigma
Param: num_rotor: how many rotors are used
	   carry_num
"""
def encodeEnigma(num_rotor,lines):
	#Variable declaration
	arr_result = []
	rotors = [] #rotors placed in the machine
	arr_shifts = [] #shift for each rotor
	arr_modulo = [] #get the modulo for your rotors
	num = 0 #general counter variable
	mirror = MIRRORS[0] #mirror to be placed in machine
	
	#Getting user's setup
	while num < num_rotor:
		string_1 = "Select a rotor from 0 to " + str(len(ROTORS)-1) + " for Rotor #" + str(num+1) + ":>"
		rotor = int(input(string_1)) 
		rotors.append(ROTORS[rotor])
		string_2 = "Init shift of Rotor #" + str(num+1) + ":>"
		shift = int(input(string_2))
		arr_shifts.append(shift)
		#Set up the modulo in fibonacci sequence ;)
		if num == 0:
			arr_modulo.append(1)
		if num == 1:
			arr_modulo.append(2)
		if num > 1:
			arr_modulo.append(arr_modulo[num-1] + arr_modulo[num-2])
		num = num + 1

	num = 0
	line_count = 0
	while line_count < len(lines):
		text = lines[line_count]
		#***************#
		result = ""
		plain_text = text
		plain_text = plain_text.upper()
		for char in plain_text:
			if char.isalpha():
				print(char)
				encoded_num = ALPHABET.index(char)
				rotor_count = 0
				#encode through rotor
				while rotor_count < len(rotors):
					rotor = rotors[rotor_count] #get the rotor
					shift = (arr_shifts[rotor_count] + encoded_num)%26 #get the corresponding shift
					encoded_num = (encoded_num + rotor[shift])%26
					if encoded_num < 0: 
						encoded_num = 26 + encoded_num
					rotor_count = rotor_count+1
					print("Encode: "+ALPHABET[encoded_num])
				#encode mirror	
				encoded_num = mirror[(encoded_num)%26]
				print("Mirror: "+ALPHABET[encoded_num])
				#going up the rotors idea: use index of, be very careful of shifts
				rotor_count = len(rotors) - 1
				while rotor_count >= 0: 
					rotor = rotors[rotor_count] #get the rotor
					encoded_num = findInput(rotor,arr_shifts[rotor_count],encoded_num)
					rotor_count = rotor_count - 1
					print("Up: "+ALPHABET[encoded_num])
				char = ALPHABET[encoded_num]
				#Set the shifts for the rotors for next char
				rotor_count = 0
				while rotor_count < len(arr_shifts):
					if num % arr_modulo[rotor_count] == 0:
						arr_shifts[rotor_count] = (arr_shifts[rotor_count] + 1)%26
					rotor_count = rotor_count+1
				print(arr_shifts)

				num = num + 1
			result += char
		arr_result.append(result)
		line_count = line_count + 1
	return arr_result

def main():
	script, plain_file, encoded_file, num_rotor = argv
	plain = open(plain_file,"r")
	encoded = open(encoded_file,"w+")
	rotor_count = int(num_rotor)
	
	input_lines = []
	output_lines = []
	for line in plain:
		input_lines.append(line)
	output_lines = encodeEnigma(rotor_count,input_lines)
	for line in output_lines:
		encoded.write(line)
	plain.close()
	encoded.close()
	print("Done!")

if __name__ == '__main__':
    main()
    