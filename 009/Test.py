def rook(start_point, end_point):
    if start_point[0] == end_point[0] or start_point[1] == end_point[1]:
        return True
    return False


def bishop(start_point, end_point):
    if abs(start_point[0] - end_point[0]) == abs(start_point[1] - end_point[1]):
        return True
    return False


def main():
    word = input('Для какой фигуру выполнить проверку:\n>> ').lower()
    a, b = map(int, input(f'Введите начальное положение для фигуры {word} ').split())
    c, d = map(int, input(f'Введите конечное положение для фигуры {word} ').split())
    if word == 'ладья':
        answer = rook((a, b), (d, c))
    elif word == 'слон':
        answer = bishop((a, b), (d, c))
    # elif :
    #     pass
    # elif:
    #     pass
    if answer:
        print(f'Ход для фигуры {word} возможен')
    else:
        print(f'Ход для фигуры {word} не возможен')


main()
