import numpy as np

option = int(input('What do you want to use? Numpy(1) or Normal(2)'))

# Function: create matrix using normal math 
def normalproc(x,y):
    c = []
    for i in range(0,x):
        r = []
        for j in range(0,y):
            r.append(i*j)
        c.append(r)
    print('The matrix is',c)

# Function: create matrix using numpy library 
def numpyproc(x,y):
    c = np.zeros((y,x))
    for i in range(0,x):
        r = []
        for j in range(0,y):
            temp = r.append(i*j)
        print(temp)
        c = np.append(c, temp, axis=1)
    print('The matrix is',c)

# Actual processing of the inputs

a = int(input('Enter number of rows of matrix:'))
b = int(input('Enter number of columns of matrix:'))

if option == 2:
    normalproc(a,b)
elif option == 1:
    numpyproc(a,b)





