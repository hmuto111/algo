def calc_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b

    return a


def calc_lcm(a, b):
    return int((a * b) / calc_gcd(a, b))


n = int(input())
a = list(map(int, input().split()))

R = calc_lcm(a[0], a[1])
for i in range(2, n):
    R = calc_lcm(R, a[i])

print(R)
