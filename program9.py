def brute_force(coeffs, x):
    return sum(coeff * (x ** i) for i, coeff in enumerate(coeffs))

def horners_method(coeffs, x):
    result = coeffs[-1]
    for coeff in reversed(coeffs[:-1]):
        result = result * x + coeff
    return result

coeffs = list(map(int, input("Enter coefficients from lowest to highest degree: ").split()))
x = int(input("Enter x: "))
print("Brute Force Result:", brute_force(coeffs, x))
print("Horner’s Method Result:", horners_method(coeffs, x))
# This code evaluates a polynomial at a given value of x using two methods: brute force and Horner's method.
# The brute force method calculates the polynomial by summing the terms, while Horner's method optimizes the evaluation by reducing the number of multiplications.