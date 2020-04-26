a = float(input())

if a >= 10:
    print("오류!")
else:
    if a < 1:
        y = 5 + a
    elif a < 5:
        y = 23 / a
    else:
        y = 5 * a
    print(y)
