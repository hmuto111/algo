n = int(input())
a = list(map(int, input().split()))

approve = True
for i in a:
    if i % 2 != 0:
        continue

    if not (i % 3 == 0 or i % 5 == 0):
        approve = False
        break

print("APPROVED" if approve else "DENIED")
