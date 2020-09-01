temp = ""
for i in range(1,int(input())+1):
    for j in str(i):
        if '3' in str(i) or '6' in str(i) or '9' in str(i):
            if j == '3' or j == '6' or j == '9':
                temp += "-"
        else:
            temp += str(j)
    temp += " "
print(temp)