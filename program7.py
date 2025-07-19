def binomial_coefficient(n, k):
    C = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1): # Initialize the table
        for j in range(min(i, k)+1): # Ensure j does not exceed k
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

n = int(input("Enter n: "))
k = int(input("Enter k: "))
print(f"C({n}, {k}) =", binomial_coefficient(n, k))
# This code calculates the binomial coefficient C(n, k) using dynamic programming.
# The function binomial_coefficient constructs a table to store intermediate results and uses them to compute the final result efficiently.