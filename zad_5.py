def check_value_in_list(my_list: list, val: int) -> bool:
    return my_list.index(val) > 0


my_list = list()
my_list.append(10)
my_list.append(9)
my_list.append(8)
my_list.append(7)
my_list.append(6)
my_list.append(5)
my_list.append(4)
my_list.append(3)
my_list.append(2)
my_list.append(1)

print(check_value_in_list(my_list, 5))
