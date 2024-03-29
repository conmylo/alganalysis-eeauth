# function to find the longest common subsequence and return the whole sequence

def lcs_sequence(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0] * (n + 1) for _ in range(m + 1)]
    # A (m+1) times (n+1) matrix to store the path
    B = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = "diagonal"
            elif C[i - 1][j] >= C[i][j - 1]:
                C[i][j] = C[i - 1][j]
                B[i][j] = "up"
            else:
                C[i][j] = C[i][j - 1]
                B[i][j] = "left"
    (i, j) = (m, n)
    lcs = []
    while i > 0 and j > 0:
        if B[i][j] == "diagonal":
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif B[i][j] == "up":
            i -= 1
        else:
            j -= 1
    return "".join(reversed(lcs))
    
X = "AGGTAB"
Y = "GXTXAYB"

lcs_ = lcs_sequence(X, Y)

print(lcs_)
print(len(lcs_))    





