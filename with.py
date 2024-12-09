f = open("file.txt")
print(f.read())
f.close()

#The same program can be written using the with statement like this:
#WITH STATEMENT
#The best way to open and close the file automatically is the with Statement.
#Open the file in the read mode using 'with', which automatically closes the files.
with open("file.txt") as f:
    print(f.read())

#We do not have to explicitly close the file as we are using the with statement.

with open("MachineLearning.txt","r") as f:
    #To Read the content of the file.
    text = f.read()
#Print the contents
print(text)