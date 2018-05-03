#decimal to factorial and back
#author: klosik007

def ReturnInt(letter):
    DictInt = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return int(DictInt.index(letter))

def ReturnString(integer):
    DictInt = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return DictInt[int(integer)]

def Factorial(number):
    result = 1
    for i in range(1, number, 1):
        result*=i
    return result

def dec2FactString(nb):
    number = nb
    div = 1
    mod = 0
    result = ""

    while (number / div >=0):
        mod = number % div
        result += ReturnString(mod)
        number /= div
        div += 1
        if (number == 0): break

    return result[::-1]

def factString2Dec(string):
    f = 1
    sum = 0
    for i in range(len(string) - 1, -1, -1):
        sum += ReturnInt(string[i]) * Factorial(f)
        f += 1
    return sum

print (dec2FactString(463))
print (factString2Dec('341010'))
