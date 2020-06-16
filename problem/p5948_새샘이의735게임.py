import sys
sys.stdin = open('./p5948.txt', 'r')


"""
1 2 3 4 5 6 7
5 24 99 76 1 77 6
"""

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    list_data = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                list_data.append(arr[i] + arr[j] + arr[k])

    list_data = list(set(list_data))
    
    for i in range(len(list_data)-1):
        for j in range(i+1, len(list_data)):
            if list_data[i] < list_data[j]:
                list_data[i], list_data[j] = list_data[j], list_data[i]
    print(f'#{t} {list_data[4]}')
