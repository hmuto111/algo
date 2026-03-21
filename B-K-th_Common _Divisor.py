a, b, k = map(int, input().split())

divisors = []
n = min(a, b)

for i in range(1, n + 1):
    if a % i == 0 and b % i == 0:
        divisors.append(i)

print(divisors[-k])
