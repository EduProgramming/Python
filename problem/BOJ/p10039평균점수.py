PEOPLE_NUM = 5
sum_num = 0
for i in range(PEOPLE_NUM):
    score = int(input())
    if score < 40:
        score = 40
    sum_num += score

print(sum_num // PEOPLE_NUM)