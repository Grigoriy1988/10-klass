list_ = [i for i in input('Введите адрес файла:\n').split('/')]
print('\n'.join(i for i in list_))


# s = input('Введите фамилию, имя и отчество:\n')
# k1 = s.find(' ')
# k2 = s.rfind(' ')
# print(s[k1+1:k1+2],'.',s[k2+1:k2+2],'.', s[:k1])