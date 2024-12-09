#WRITE FILES IN PYTHON

#In order to write to a file, we first open it in write or append mode after which we can use the python's f.write() method to write to the file!

#Open the file in the write mode.
f=open("MachineLearning.txt","w")
#Write a string to the file
f.write("Machine Learning is the subset of the Artificial Intelligence.")
#Close the file
f.close()