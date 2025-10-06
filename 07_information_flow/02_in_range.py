def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    else:
        return False


# Test the function
print(in_range(5, 1, 10))    # True (5 is between 1 and 10)
print(in_range(1, 1, 10))    # True (1 is at lower bound)
print(in_range(10, 1, 10))   # True (10 is at upper bound)
print(in_range(0, 1, 10))    # False (0 is below range)
print(in_range(11, 1, 10))   # False (11 is above range)
