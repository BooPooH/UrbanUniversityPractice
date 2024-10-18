my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
list_length = len(my_list)
current_index = 0
while current_index != list_length and my_list[current_index] >= 0:
    current_index = current_index + 1
    if my_list[current_index - 1] == 0:
        continue
    print(my_list[current_index - 1])
# ну или так
# while current_index < list_length:
#     if my_list[current_index] < 0:
#         break
#     elif my_list[current_index] > 0:
#         print(my_list[current_index])
#     current_index = current_index + 1