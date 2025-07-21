def warshalls(adj_matrix, n):
    # Apply Warshall's Algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j]):
                    adj_matrix[i][j] = 1

    # Print the Transitive Closure
    print("The transitive closure of the graph is:")
    for i in range(n):
        for j in range(n):
            print(adj_matrix[i][j], end=" ")
        print()

# Main function
def main():
    n = int(input("Enter the number of vertices: "))
    adj_matrix = []

    print("Enter the adjacency matrix row by row (space separated):")
    for i in range(n):
        row = list(map(int, input().split()))
        adj_matrix.append(row)

    warshalls(adj_matrix, n)

# Run the program
main()
