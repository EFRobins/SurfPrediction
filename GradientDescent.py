import decimal


def find_cost(X, Y, gradient, bias):
    N = len(X)
    error = 0
    try:
        for i in range(N):
            error += ((Y[i - 1] - (gradient * X[i - 1] + bias)) ** 2)     # fix for dataset added times 0.5
        error = error / N
        return round(error, 3)
    except OverflowError:
        print(":(")


def deriv_weight(X, Y, gradient, bias):
    n = len(Y)
    derivative = 0
    for i in range(n):
        derivative += X[i] * ((gradient * X[i-1] + bias) - Y[i-1]) #swapped the subtraction part
    derivative = 2 * derivative / n
    return derivative


def derivative_bias(X, Y, gradient, bias):
    N = len(Y)
    derivative = 0
    for i in range(N):
        derivative += ((gradient * X[i - 1] + bias) - Y[i - 1])
    derivative = 2 * derivative / N
    return derivative


def update_gradient(gradient, lr, derivative):
    gradient -= round(lr * derivative, 5)
    return gradient

def update_bias(bias, lr, derivative):
    bias -= round(lr * derivative, 5)
    return bias


def cleanlist(list):
    x = ""
    real_X = []
    for i in list:
        for y in i:
            try:
                float(y)
                x += str(y)
            except SyntaxError:
                continue
        real_X.append(float(x))
        x = ""
    return real_X
