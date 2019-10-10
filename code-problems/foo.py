a = "abcef"
b = "ab"


for x in range(0, len(a)-len(b), len(b)):
    print(x)  # 0, 0+2, 0+2+2
