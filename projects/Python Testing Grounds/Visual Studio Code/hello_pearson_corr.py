import numpy as np

def find_corr(X, Y, type = "pearson"):
    corr = 0
    if type.__contains__("pearson"):
        print("Correlation Type: \"Pearson\"")
        sum_x           = 0
        sum_y           = 0
        sum_xy          = 0
        sum_x_squared   = 0
        sum_y_squared   = 0
        n               = len(X)  # = len(Y)
        
        for i in range(0,n):
            print(X[i], ", ", Y[i])
            sum_x           = sum_x + X[i]
            sum_y           = sum_y + Y[i]
            sum_xy          = sum_xy + (X[i] * Y[i])
            sum_x_squared   = sum_x_squared + np.power(X[i],2)
            sum_y_squared   = sum_y_squared + np.power(Y[i],2)
        
        numerator   = (sum_xy - (sum_x * sum_y) / n)
        denominator = np.sqrt((sum_x_squared - np.power(sum_x, 2) / n) * (sum_y_squared - np.power(sum_y, 2) / n))
        corr = numerator / denominator
        
    return corr
            
            
corr = find_corr(X = [1,2,3], Y = [3,2,1])

print(corr)

