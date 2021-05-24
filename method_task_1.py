def average_x(arr):
    X_av=sum(arr)/len(arr)
    return X_av

def x_multiply_x(arr):
    X_multiply=[]
    for i in range(len(arr)):
        X_multiply.append(arr[i]*arr[i])
    return sum(X_multiply)

def dispersion(arr,x_av,sum_x_multi):
    D=sum_x_multi/len(arr)-(x_av * x_av)
    return D

def corrected_deviation(arr,d):
    SS=len(arr)/(len(arr)-1)*d
    return SS