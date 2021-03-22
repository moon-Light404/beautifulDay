#1.有四个数，相加等于45，分别去+2 -2 *2 /2得到的结果相等，求这四个数
for a in range(1,46):
    for b in range(1,46):
        for c in range(1,46):
            for d in range(1,46):
                if a + b + c + d == 45 and a + 2 == b - 2 and b - 2 == c * 2 and c * 2 == d / 2:
                    print(f'这四个数是{a},{b},{c},{d}')
