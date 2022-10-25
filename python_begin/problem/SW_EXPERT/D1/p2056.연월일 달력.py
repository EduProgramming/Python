T = int(input())
for t in range(1, T+1):
    M = input()
    year = M[0:4]
    month = M[4:6]
    day = M[6:8]
    res =1
    if int(month) == 2 and int(day) > 28:
        res = -1
    elif int(month) >12 or int(month) < 1:
        res = -1
    elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
        if int(day) > 31 or int(day) < 1:
	        res = -1
    elif int(month) == 2 or int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        if int(day) > 30 or int(day) < 1:
	        res = -1

    if res == 1:
        res = year+"/"+month+"/"+day

    print("#{} {}".format(t, res))

# #다른방법2
# T=int(input())
# days=[31,28,31,30,31,30,31,31,30,31,30,31]
# for t in range(1, T+1):
#     M=input()
#     month=M[4:6]
#     day=M[6:8]
#     if M[:4]=='0000' or int(day)>32 or int(month)>12 or month=='00' or day=='00' or int(day)>days[int(month)-1] :
#         print("#{} -1".format(t))
#     else:
#         print("#{} {}/{}/{}".format(t, M[:4], month, day))