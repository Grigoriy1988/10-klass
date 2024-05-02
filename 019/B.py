def B(name, ext):
    if '.' not in name:
        return name + '.' + ext
    k = name.rfind('.')
    return name[:k + 1] + ext


name = input('Введите имя файла:')
extension = input('Введите новое расширение:')
print(f'Результат:{B(name, extension)}')
