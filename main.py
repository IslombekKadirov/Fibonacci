def fibonacci(n):
    l = []
    while len(l)<n:
        if len(l)<2:
            l.append(1)
        else:
            l.append(l[-1]+l[-2])
    print(*l)
fibonacci(int(input()))