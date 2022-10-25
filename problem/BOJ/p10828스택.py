import sys
input = sys.stdin.readline

stack = []

def push(item):
    stack.append(item)

def pop():
    if stack:
        return stack.pop()
    return -1

def size():
    print(len(stack))

def empty():
    if stack:
        print(0)
    else:
        print(1)

def top():
    if stack:
        print(stack[-1])
    else:
        print(-1)

for i in range(int(input())):
    cmd = input().split()
    if len(cmd) > 1: # push
        push(int(cmd[-1]))
    else:
        if cmd[0] == 'pop':
            print(pop())
        elif cmd[0] == 'size':
            size()
        elif cmd[0] == 'empty':
            empty()
        elif cmd[0] == 'top':
            top()
