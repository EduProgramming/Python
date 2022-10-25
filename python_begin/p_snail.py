N = int(input())

# N = 5
x = -1
y = 0
num = 0
switch = 1
arr = [[0] * N for _ in range(N)]

write = N

while write > 0:
    # 오른쪽 방향
    for i in range(write):
        num += 1
        x += switch
        arr[y][x] = num

    write -= 1 # 위/아래 향할 때

    # 아래방향
    for i in range(write):
        num += 1
        y += switch
        arr[y][x] = num

    switch = -1 * switch

for data in arr:
    print(data)