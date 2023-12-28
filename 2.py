DESCRIPTIO

N

:

Numpy Eigenvalue is a function in the numpy linear algebra package of the numpy library

which is used to generate the Eigenvalues or Eigenvectors from a given real symmetric or

complex symmetric array or matrix given as input to the function. Depending upon the

kind of input array or matrix the numpy eigenvalue function returns two type of arrays,

one dimensional array representing the eigenvalues in the position of the input and another

two dimensional array giving the eigenvector corresponding to the columns in the input

matrix

.

PROGRAM:

import numpy as np

row,col=list(map(int,input('Enter 

row and col').split()))

A=np.array(list(map(int,input('Enter matrix A').split())))

A.shape=(int(row),int(col))

print("Given Array=",A)

print("Transpose=",np.transpose(A))
