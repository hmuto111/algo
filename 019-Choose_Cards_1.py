def combination(n, r):
    nt = 1
    rt = 1
    for i in range(1, r + 1):
        nt = nt * (n - i + 1)
        rt = rt * i

    return int(nt / rt)


n = int(input())
a = list(map(int, input().split()))

aggregation = {
    1: combination(a.count(1), 2),
    2: combination(a.count(2), 2),
    3: combination(a.count(3), 2),
}

ans = aggregation[1] + aggregation[2] + aggregation[3]

print(ans)
