import math

def fx(x):
    return math.pow(x , 3) - (32 * x) + 8


def mullers(x_0 , x_1 , x_2 , allowed_error):
    h_0 = x_1 - x_0
    h_1 = x_2 - x_1
    d_0 = (fx(x_1) - fx(x_0)) / h_0
    d_1 = (fx(x_2) - fx(x_1)) / h_1
    a = (d_1 - d_0) / (h_0 + h_1)
    b = (a * h_1) + d_1
    c = fx(x_2)
    if b < 0:
        x_3 = x_2 + ((-2 * c)/(b - (math.sqrt((b * b) - (4 * a * c)))))
    else:
        x_3 = x_2 + ((-2 * c)/(b + (math.sqrt((b * b) - (4 * a * c)))))
    error = (x_2 - x_3) / x_3
    if error <= allowed_error:
        return x_3
    else:
        return mullers(x_1 , x_2 , x_3 , 0.0005)
    
x_0 = 7
x_1 = 6
x_2 = 1
allowed_error = 0.0005
print("The root of the equation is ", mullers(x_0 , x_1 , x_2 , allowed_error))


