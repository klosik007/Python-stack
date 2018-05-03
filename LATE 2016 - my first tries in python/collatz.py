def collatz(number):
    if number %2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Type an integer value')
try:
    num = int(input())
except ValueError:
    print('Type an integer!')

while collatz(num) != 1:
    num = collatz(num)
    print(num)
    
print('1')

    



       
