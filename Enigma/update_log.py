from datetime import datetime
from sys import argv


def main():
	script, file_name = argv #Arguments processing
	print("Update the file line-by-line. Type Done when completed")
	file = open(file_name,"a+") #Open the file for appending
	typed = "" #init var
	lines = [] #init list
	
	#read the inputs line by line into lines
	while True:
		typed = input(">")
		if typed == "Done" or typed == "done":
			break
		else: 
			lines.append(typed)

	file.write("=================\n")
	file.write(datetime.now().strftime('%m-%d-%Y %H:%M:%S') + "\n")
	file.write("=================\n")
	for line in lines: 
		file.write("+ " + line + "\n")

	file.write("*****************\n")
	file.write("\n")
	file.close()

if __name__ == '__main__':
    main()