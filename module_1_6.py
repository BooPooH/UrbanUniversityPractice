my_dict = {'Name1':888,'Name2':666,'Name3':999}
print(my_dict)
print("значение по существующему ключу :",my_dict['Name1'])
print("значение по отсутствующему ключу:",  my_dict.get('Name'))
my_dict.update({'Name4':777,'Name5':111})
popitem = my_dict.pop('Name2')
print("значение удалённого ключа",popitem)
print(my_dict)

my_set = {1, 2 ,3 ,3 ,2, 'a', 'b', 'ab', 'ab','cb', 5, 7,7}
print(my_set)
my_set.update([101, 'abc'])
my_set.remove(3)
print(my_set)