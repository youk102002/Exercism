def flatten(iterable):
    flatten_list = []
    for element in iterable:
        if isinstance(element, (list, tuple, set)):
            flatten_list.extend(flatten(element))
        elif element is not None:
            flatten_list.append(element)
    return flatten_list