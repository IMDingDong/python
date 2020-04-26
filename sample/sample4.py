a = int(input())
x = float(input())
y = float(input())

if a in [3, 15, 25]:
    x = x / 4
    y = y ** 5
elif 7 <= a <= 12:
    x = x * 3
    y += 1
elif a > 52:
    x = x % 4
    y += 9
else:
    x -= 9
    y += 1

print(x, y)
