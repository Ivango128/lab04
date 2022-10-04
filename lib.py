a = list('b f d s j k l B J F  N DS B K N a k l d n k n d s j k n'.split(' '))
b = list('d  d d  d d ew fhjhw b w hfhh hf iw  f  f h   c sa  d gt'.split(' '))
c = list('d  d d  d d ew f h  j h w b w h f h h h f i w  f  f h   c s a  d g t'.split(' '))

matrix = list()
n = int(input('Введите кол-во входных списков '))
# matrix.append(a)
# matrix.append(b)
# matrix.append((c))
while n > 0:
    matrix.append(input('Введите элементы списка через пробел.\n').split(' '))
    n -=1

def serch(matrix):
    i = 0
    index = 0
    min = len(matrix)
    for spisok in matrix:
        if len(spisok) < min:
            min = len(spisok)
            index = i
        i +=1
    return index
    #matrix1.append(matrix[index])


index = serch(matrix)
povtor = list()


def povtorenia(matrix, index):
    run = True
    j = 0
    while run:
        try:
            for i in range(len(matrix[index])):
                if matrix[index][i] in matrix[j]:
                    if matrix[index][i] in povtor:
                        None
                    else:
                        povtor.append(matrix[index][i])
            j +=1
        except IndexError:
            run = False

    return povtor

if len(povtorenia(matrix, index)) > 0:
    print('Повторяюшееся символы ',povtorenia(matrix, index))
else:
    print('Повторений нет!')