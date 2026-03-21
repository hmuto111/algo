n = int(input())
a = list(map(int, input().split()))

aggregation = {
    100: a.count(100),
    200: a.count(200),
    300: a.count(300),
    400: a.count(400),
}

ans = (aggregation[100] * aggregation[400]) + (aggregation[300] * aggregation[200])

print(ans)
