import sys
input = sys.stdin.readline

stack = []
high = -1

def push(num) :
    global high
    stack.append(num)
    high += 1

def top() :
    if len(stack) == 0 :
        print(-1)
    else :
        print(stack[high])

def userDefPop() :
    global high
    if high == -1 :
        print(-1)
    else :
        print(stack.pop())
        high -= 1


n = int(input().rstrip())


for _ in range(n):
    command = input().rstrip()

    if "push" in command :
        command = command.split()
        push(command[1])

    if command == "top" :
        top()

    if command == "size" :
        print(len(stack))

    if command == "pop" :
        userDefPop()

    if command == "empty" :
        print(1) if high == -1 else print(0)