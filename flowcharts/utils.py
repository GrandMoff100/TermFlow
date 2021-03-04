def collapse_list(iterable):
    for i in iterable:
        yield from i

def truecenter(x, i):
    return ' ' * ((i + 1) % 2)  + x.center(i)[:i + (i + 1) % 2]
