def calc_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b

    return a


n = int(input())
a = list(map(int, input().split()))

R = calc_gcd(a[0], a[1])
for i in range(2, n):
    R = calc_gcd(R, a[i])

print(R)
