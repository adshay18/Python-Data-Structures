def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    min = None
    max = None
    key_set = set(d.keys())
    
    for key in key_set:
        if min == None or key < min:
            min = key
        if max == None or key > max:
            max = key
    return (min, max)