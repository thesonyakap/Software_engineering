def get_entry_period(tpl, elem):
    if elem not in tpl:
        return ()
    first = tpl.index(elem)
    try:
        second = tpl.index(elem, first + 1)
        return tpl[first:second + 1]
    except ValueError:
        return tpl[first:]

print(get_entry_period((1, 2, 3), 8))
print(get_entry_period((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(get_entry_period((1, 2, 8, 5, 1, 2, 9), 8))
