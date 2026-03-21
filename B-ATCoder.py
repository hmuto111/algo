s = input()

ok = {"A", "C", "G", "T"}
cur = 0
best = 0

for ch in s:
    if ch in ok:
        cur += 1
        if cur > best:
            best = cur
    else:
        cur = 0

print(best)
