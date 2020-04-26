print("1. 빨간색")
print("2. 녹색")
print("3. 파란색")
print("4. 흰색")
print("5. 검정색")
print("6. 회색")
color = int(input("색을 선택하여라: "))

print("선택한 색에 대한 RGB 코드: ")

if color == 1:
    print("FF0000")
else:
    if color == 2:
        print("00FF00")
    else:
        if color == 3:
            print("0000FF")
        else:
            if color == 4:
                print("FFFFFF")
            else:
                if color == 5:
                    print("000000")
                else:
                    if color == 6:
                        print("7F7F7F")
                    else:
                        print("모르는 색입니다.")
