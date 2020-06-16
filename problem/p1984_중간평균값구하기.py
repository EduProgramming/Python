import sys
sys.stdin = open('p1984.txt', 'r')

T = int(input())
for t in range(1, T+1):
    numbers = list(map(int ,input().split()))
    max_num = numbers[0]
    min_num = numbers[0]
    sum_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
        sum_num += num

    sum_num = sum_num - (max_num + min_num)
    result = round(sum_num / (len(numbers) - 2))
    print(f'#{t} {result}')
