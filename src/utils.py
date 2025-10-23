def add(*args):
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


def multiply(*args):
    """Return product of args. If a single iterable provided, multiply items."""
    if len(args) == 1 and isinstance(args[0], Iterable) and not isinstance(args[0], (str, bytes)):
        nums = list(args[0])
    else:
        nums = list(args)
    if not nums:
        return 1
    prod = 1.0
    for n in nums:
        prod *= float(n)
    return prod

def divide(a, b, *rest):
    """Divide a by b, then by any rest in order. Raises ZeroDivisionError on divide by zero."""
    nums = [a, b] + list(rest)
    nums = [float(x) for x in nums]
    result = nums[0]
    for n in nums[1:]:
        if n == 0:
            raise ZeroDivisionError("division by zero")
        result /= n
    return result

