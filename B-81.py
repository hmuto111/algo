n = int(input())

e = any(i * j == n for i in range(1, 10) for j in range(1, 10))

print("Yes" if e else "No")
