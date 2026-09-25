# Practical 6
# Implementation of Chain Matrix Multiplication
# using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # m[i][j] stores minimum multiplication cost
    m = [[0] * n for _ in range(n)]

    # s[i][j] stores the position where the chain is split
    s = [[0] * n for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            # Initialize with infinity
            m[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


# Function to print the optimal parenthesization
def print_optimal_parenthesis(s, i, j):

    if i == j:
        print(f"A{i + 1}", end="")
        return

    print("(", end="")

    print_optimal_parenthesis(s, i, s[i][j])
    print_optimal_parenthesis(s, s[i][j] + 1, j)

    print(")", end="")


# Main program
print("CHAIN MATRIX MULTIPLICATION USING DYNAMIC PROGRAMMING")
print("-" * 55)

# Dimensions of matrices
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60
# A4 = 60 x 10

p = [10, 30, 5, 60, 10]

m, s = matrix_chain_order(p)

n = len(p) - 1

print("\nMatrix Dimensions:")

for i in range(n):
    print(f"A{i + 1} = {p[i]} x {p[i + 1]}")

print("\nMinimum number of scalar multiplications:", m[0][n - 1])

print("Optimal Parenthesization: ", end="")
print_optimal_parenthesis(s, 0, n - 1)

print("\n")