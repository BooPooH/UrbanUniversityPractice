def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1
print_params()
print_params(True)
print_params('oops', "i")
print_params('did', 'it', 'again')
print_params(b=25)
print_params(c=[1, 2, 3])
# 2
values_list = ["Yes", False, 666]
values_dict = {'a': True, 'b': 777, 'c': "No"}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = ["Urban", 10]
print_params(*values_list_2, 42)
