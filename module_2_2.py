print("Введите три целых числа")
first = input("1): ")
second = input("2): ")
third = input("3): ")
if first == second and second == third:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)