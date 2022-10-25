import sys
sys.stdin = open('p1989.txt', 'r')

T = int(input())
for t in range(1, T+1):
    data = input()
    result = 1
    for i in range(len(data)//2+1):
        if data[i] != data[-i-1]:
            
            result = 0
            break
    print(f'#{t} {result}')

# l   e  v  e  l
# 0   1  2  3  4
# -5 -4 -3 -2 -1