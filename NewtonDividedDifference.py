import math as m

n = int(input("Enter the order of the interpolation function: "))
c = float(input("Enter value of x at which interpolation needs to be performed: "))

x = [float(i) for i in input("Enter values of x_i's : ").split()]
f = [float(i) for i in input("Enter values of f(i) : ").split()]

def divideddiff(k, f):
    result = 0
    for i in range(k + 1):
        alphainv = 1
        for j in range(k + 1):
            if i != j:
                alphainv = alphainv * (x[i] - x[j])
        alpha = 1 / alphainv
        result += alpha * f[i]
    return result


def fun():
    result = 0
    for i in range(n + 1):
        temp_prod = 1
        for j in range(i):
            temp_prod *= (c - x[j])
        result = result + divideddiff(i, f) * temp_prod
    return result

val = fun()
interpolated_val=val
print(f"The interpolated value at x = {c} is: {interpolated_val}")