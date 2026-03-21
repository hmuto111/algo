n = int(input())

r = len(str(n))
answer = 0

for i in range(0, r + 1):
    if i % 2 == 0:
        continue

    start = 10 ** (i - 1)
    end = 10**i - 1

    if end > n:
        end = n

    answer = answer + (end - start + 1)

print(answer)
