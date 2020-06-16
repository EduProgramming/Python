import sys
sys.stdin = open('p2005.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    result = [[1 for col in range(row+1)] for row in range(N)]

    for i in range(1, N):
        for j in range(i+1):
            if j == 0 or j == i:
                result[i][j] = 1
            else:
                result[i][j] = result[i-1][j-1] + result[i-1][j]
    
    print('#' + str(t))
    for i in range(N):
        for j in range(i+1):
            print(result[i][j], end=" ")
        print()

        


"""
1           1
1 1         2
1 2 1       3
1 3 3 1
"""