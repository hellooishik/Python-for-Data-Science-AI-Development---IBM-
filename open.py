file = open('example.txt' , 'r')
# file_stuff = file.read()
# line1 = file.readline()  # Reads the first line
# line2 = file.readline()  # Reads the second line
# print(line1 + line2);

file.seek(7) 
characters = file.read(5) 
print(characters)
file.close()