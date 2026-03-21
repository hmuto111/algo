n = int(input())
a = list(map(int, input().split()))
history = {}

cnt = 0
for i in a:
    p = 100000 - i

    if p in history:
        cnt += history[p]

    if i in history:
        history[i] += 1
    else:
        history[i] = 1

# print(history)

print(int(cnt))
