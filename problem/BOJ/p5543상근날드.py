min_hamburger = 2000
min_juice = 2000

for i in range(3):
    hamburger = int(input())
    # if min_hamburger > hamburger:
    #     min_hamburger = hamburger
    min_hamburger = hamburger if min_hamburger > hamburger else min_hamburger

for i in range(2):
    juice = int(input())
    # if min_juice > juice:
    #     min_juice = juice
    min_juice = juice if min_juice > juice else min_juice

result = min_hamburger + min_juice - 50

print(result)