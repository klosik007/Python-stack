def write_string(lista):
    for i in range(len(lista)- 1):
        print(lista[i], end=', ')
    print('and ' + lista[len(lista) - 1], end='.')

spam = ['apples', 'bananas', 'tofu', 'cats']
write_string(spam)


