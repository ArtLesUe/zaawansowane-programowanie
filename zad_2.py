def values_in_array_by_2_version_a(values_list: list):
    new_list = list()
    for value in values_list:
        new_list.append(value * 2)
    return new_list


def values_in_array_by_2_version_b(values_list: list):
    return [value * 2 for value in values_list]


values_list = list()
values_list.append(5)
values_list.append(10)
values_list.append(15)
values_list.append(20)
values_list.append(25)

print(values_in_array_by_2_version_a(values_list=values_list))
print(values_in_array_by_2_version_b(values_list=values_list))
