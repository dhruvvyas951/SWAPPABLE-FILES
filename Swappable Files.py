import os

file1 = input("Enter file 1 directory: ")
file2 = input("Enter file 2 directory: ")

def swapableFiles():

    with open(file1, 'r') as f:
        data_a = f.read()
    with open(file2, 'r') as f:
        data_b = f.read()       
    with open(file1, 'w') as f:
        f.write(data_b)
    with open(file2, 'w') as f:
        f.write(data_a)

swapableFiles()