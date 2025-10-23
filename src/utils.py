def add(*args):
    print("DEBUG: add function called")
    """
    Return the sum of all numeric arguments.
    If no arguments are provided, return 0.
    """
    total = 0
    for x in args:
        total += x
    return total


def subtract(*args):
    """
    Subtract all subsequent args from the first one.
    If no arguments are provided, return 0.
    """
    if not args:
        return 0
    result = args[0]
    for x in args[1:]:
        result -= x
    return result
