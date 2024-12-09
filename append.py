#WRITE FILES IN PYTHON

#In order to write to a file, we first open it in write or append mode after which we can use the python's f.write() method to write to the file!



st = "Machine Learning is the Subset of the Artificial Intelligence and it plays a vital role in today's world."
f = open("myfile.txt", "a")
f.write(st)
f.close()