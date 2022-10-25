import sys
sys.stdin = open('p1976.txt', 'r')

T = int(input())
for t in range(1, T+1):
    """
    3 17 1 39
    8 22 5 10
    6 53 2 12   
    """
    h1, m1, h2, m2 = list(map(int, input().split()))
    hour = h1 + h2
    minute = m1 + m2
    if minute >= 60:
        hour += 1
        minute -= 60
    
    if hour > 12:
        hour -= 12
    print(f'#{t} {hour} {minute}')