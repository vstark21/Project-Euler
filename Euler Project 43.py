import collections
import math

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numPossible = []
for i in num:
    num1 = num.copy()
    num1.remove(i)
    for j in num1:
        num2 = num1.copy()
        num2.remove(j)
        for k in num2:
            num3 = num2.copy()
            num3.remove(k)
            for l in num3:
                num4 = num3.copy()
                num4.remove(l)
                for m in num4:
                    num5 = num4.copy()
                    num5.remove(m)
                    for n in num5:
                        num6 = num5.copy()
                        num6.remove(n)
                        for o in num6:
                            num7 = num6.copy()
                            num7.remove(o)
                            for p in num7:
                                num8 = num7.copy()
                                num8.remove(p)
                                for q in num8:
                                    num9 = num8.copy()
                                    num9.remove(q)
                                    for r in num9:
                                        temp = int(i + j + k + l + m + n + o + p + q + r)
                                        if len(str(temp)) == 10:
                                            numPossible.append(temp)

numPattern = []
primes = [2, 3, 5, 7, 11, 13, 17]
for num in numPossible:
    temp = str(num)
    for i in range(len(primes)):
        if int(temp[1 + i:4 + i]) % primes[i] == 0:
            pass
        else:
            break
    else:
        numPattern.append(num)
    print(num)

print(numPattern)
print(sum(numPattern))
