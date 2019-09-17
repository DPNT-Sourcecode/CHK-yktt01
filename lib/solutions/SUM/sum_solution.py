# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y:int) -> int:
    if x < 0 or x > 100 or y < 0 or y > 100:
        error_str = "The parameters for sum_solution should be between 0 and 100"
        error_str += " but are {0}, {1}".format(x, y)
        raise ValueError(error_str)
    return x + y

