def delete(list_, index=None):
    if index != None:
        new_list1 = list_[:index]  # TODO реализовать функцию удаления элемента из списка по индексу
        new_list2 = list_[index + 1:]
        new_list = new_list1 + new_list2
    else:
        new_list = list_[:len(list_) - 1]
    return new_list


# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
