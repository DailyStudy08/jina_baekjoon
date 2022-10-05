while True:
    str=input()
    if str=='.':
        break
    stack=[]
    answer='yes'
    for s in str:
        if s=='(' or s=='[':
            stack.append(s)
        elif s==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                answer='no'
                break
        elif s==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                answer='no'
    if stack:
        answer='no'
    print(answer)
