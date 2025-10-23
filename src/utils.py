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


def add(*args):
    """Return sum of all args. Accepts numbers or an iterable as single arg."""
    # handle a single iterable argument like add([1,2,3])
    if len(args) == 1 and isinstance(args[0], Iterable) and not isinstance(args[0], (str, bytes)):
        nums = list(args[0])
    else:
        nums = list(args)
    if not nums:
        return 0
    return sum(float(x) for x in nums)

def subtract(*args):
    """If one arg: return -arg. If many: subtract in order: a - b - c ..."""
    if len(args) == 1 and isinstance(args[0], Iterable) and not isinstance(args[0], (str, bytes)):
        nums = list(args[0])
    else:
        nums = list(args)
    if not nums:
        raise ValueError("subtract requires at least one value")
    nums = [float(x) for x in nums]
    if len(nums) == 1:
        return -nums[0]
    result = nums[0]
    for n in nums[1:]:
        result -= n
    return result

