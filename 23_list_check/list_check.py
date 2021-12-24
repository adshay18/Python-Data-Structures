def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    num_to_check = len(lst)
    num_true = 0
    for item in lst:
        if type(item) is list:
            num_true += 1
        
    if num_true == num_to_check:
        return True
    else:
        return False