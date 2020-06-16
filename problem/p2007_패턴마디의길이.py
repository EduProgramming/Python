import sys
sys.stdin = open('p2007.txt', 'r')

T = int(input())
for t in range(1, T+1):
    data = input()
    result = 0
    for i in range(1, 11):
        if data[:i] == data[i:2*i]:
            result = len(data[:i])
            break
    
    print(f'#{t} {result}')