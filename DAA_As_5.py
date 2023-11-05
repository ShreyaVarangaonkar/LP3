N = int(input("Enter the number of queens: "))
print("Entered number of queens:", N)

# Initialize the chessboard as an NxN matrix with all elements set to 0
board = [[0] * N for _ in range(N)]

def is_attack(i, j):
    # Check if there is a queen in the same row or column
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Check diagonals
    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def N_queen(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if not is_attack(i, j) and board[i][j] != 1:
                board[i][j] = 1

                if N_queen(n - 1):
                    return True
                board[i][j] = 0
    return False

if N_queen(N):
    print("Solution for", N, "- Queens Problem:")
    for i in board:
        print(i)
else:
    print("No solution found for", N, "- Queens Problem.")
