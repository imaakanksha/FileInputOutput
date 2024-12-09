'''
The random-access memory is volatile, and all its contents are lost once a program terminates in order to persist the data forever, we use files.
A file is data stored in a storage device. A python program can talk to the file by reading content from it and writing content to it.
RAM = Volatile
HDD/SDD/Hrddisk/Pendrive = Non Volatile
TYPES OF FILES
There are 2 types of files:
1)Text Files (.txt, .c etc.)
2)Binary Files(.jpg, .dat, etc.)
Python has a lot of functions for reading, updating, and deleting files.

OPENING A FILE
Python has an open() function for opening files. It takes 2 parameters: filename and made
'''
#READING A FILE IN PYTHON
#open the file in read mode
f = open("file.txt","r")
#Read its contents
data = f.read()
#Print its contents
print(data)
#close the file
f.close()

#OTHER METHODS TO READ THE FILE
#We can also use f.readline() function to read one full line at a time.
#f.readline() = Read one line from the file.
'''
MODES OF OPENING A FILE

r = open for reading
w = open for writing
a = open for appending
+ = open for updating
'rb' will open for read in binary mode
'rt' will open for read in text mode.

'''

f = open("file.txt")
lines=f.readlines()
print(lines, type(lines))
f.close()

# line1=f.readline()
# print(line1, type(line1))

# line2=f.readline()
# print(line2, type(line2))

# line3=f.readline()
# print(line3, type(line3))

# line4=f.readline()
# print(line4, type(line4))

# line5=f.readline()
# print(line5 == "")

# line=f.readline()
# while(line != ""):
#     print(line)
#     line=f.readline()

# f.close()
