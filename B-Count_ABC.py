n = int(input())
s = input()

c = "ABC"

answer = 0

for i in range(n - 2):
    if n < 3:
        break

    tmp = s[i : i + 3]
    if c == tmp:
        answer += 1

print(answer)
