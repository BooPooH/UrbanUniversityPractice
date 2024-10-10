immutable_var = (1, 'string', 2.0 , False, [0,True,'Dva'])
print('Immutable tuple: ',immutable_var)
# immutable_var[1] = 'lol' данная строка выдаст ошибку: 'tuple' object does not support item assignment
mutable_list = [1, 99, 'str', 0.111, True]
print('Mutable list: ',mutable_list)
mutable_list[0] = 'Odin'
mutable_list[4] = False
print('Mutable list после изменений:',mutable_list)