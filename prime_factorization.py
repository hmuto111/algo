n = int(input())
answer = []
limit = int(n**0.5)

for i in range(2, limit + 1):

    while n % i == 0:
        answer.append(i)
        n = n / i

if n >= 2:
    answer.append(int(n))

print(*answer)
