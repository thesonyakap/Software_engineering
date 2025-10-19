def remove_element(tpl, value):
    if value in tpl:
        lst = list(tpl)
        lst.remove(value) 
        return tuple(lst)
    return tpl

print(remove_element((1, 2, 3), 1))
print(remove_element((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_element((2, 4, 6, 6, 4, 2), 9))
