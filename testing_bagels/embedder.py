import numpy as np
from numpy import linalg as ln

def calculate_eigenvalues(m1):
    eigenvalues = ln.eig(m1)[0]
    return(eigenvalues)

def biggest_eigenvalue(m1):
    return(calculate_eigenvalues(m1)[0])

def smallest_eigenvalue(m1):
    return(min(calculate_eigenvalues(m1)))

def sum_eigenvalues(m1):
    return(sum(calculate_eigenvalues(m1)))

def embed(m1):
    vec = [sum_eigenvalues(m1), biggest_eigenvalue(m1), smallest_eigenvalue(m1)]
    return(vec)


A = np.matrix("1 0 0; 0 1 0; 0 0 1")

print(embed(A))
