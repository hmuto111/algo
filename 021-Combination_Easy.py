n, r = map(int, input().split())

nt = 1
rt = 1
for i in range(1, r + 1):
    nt = nt * (n - i + 1)
    rt = rt * i

ans = int(nt / rt)
print(ans)
