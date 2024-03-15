import sys 
input = sys.stdin.readline

n = int(input())    # 명령어 개수 입력
lst = [input() for _ in range(n)]   # 명령어 입력

stack = []  # 스택 초기화

for l in lst:   # 각 명령어 수행
    s = sys.stdin.readline().split() 
    if s[0] == 'push': # push X: 정수 X를 스택에 넣는 연산이다. 만약 명령어가 push 연산이면
        stack.append(s[1])  # 해당 숫자를 스택에 넣고
    elif s[0] == 'pop': # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stack)>0: print(stack.pop()) # 스택이 비어있지 않다면 > 가장 위의 값을 스택에서 빼내어 출력
        else: print(-1) # 아니면 -1 출력
    elif s[0] == 'size':    # size: 스택에 들어있는 정수의 개수를 출력한다.
        print(len(stack))   # 스택의 크기 출력
    elif s[0] == 'empty':   # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack)==0: print(1)  # 비어있으면 1 출력
        else: print(0)  # 아니면 0 출력
    elif s[0] == 'top': # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
        if len(stack)>0: print(stack[-1])   # 비어있지 않으면 > 가장 위의 값을 스택에서 빼내어 출력
        else: print(-1)  # 아니면 -1 출력 