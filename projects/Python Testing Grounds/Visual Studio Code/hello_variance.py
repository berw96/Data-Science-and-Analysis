import numpy as np

def find_variance(X):
    variance        = 0
    sum_x           = 0
    sum_x_squared   = 0
    mean_x          = 0
    n               = len(X)
    
    for i in range(0,n):
        sum_x_squared   = sum_x_squared + np.power(X[i], 2)
        sum_x           = sum_x + X[i]
    
    mean_x      = sum_x / n
    numerator   = sum_x_squared - n * np.power(mean_x, 2)
    denominator = n
    variance    = numerator / denominator
    
    return variance

variance = find_variance(X = [1,1,2,45,1])

print(variance)

