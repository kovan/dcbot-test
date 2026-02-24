def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def identity(x):
    return x


def compose(f, g):
    return lambda x: f(g(x))
