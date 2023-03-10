import numpy as np 

def lrt(T):
    p1 = np.array([0.5,0.35,0.15])
    p2 = np.array([0.2,0.3,0.5])
    lr = p1 / p2
    A = np.zeros(len(p1))
    A_c = np.ones(len(p1))
    for i in range(len(lr)):
        if lr[i] > T:
            A[i] = 1 
            A_c[i] = 0 
    alpha = 0 
    beta = 0 
    for i in range(len(lr)):
        if A_c[i] == 1:
            alpha += p1[i]
        if A[i] == 1:
            beta += p2[i] 
    return alpha,beta  
