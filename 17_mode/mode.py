def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_set = set(nums)
    num_count = dict.fromkeys(num_set, 0)
    mode = 0
    for num in nums:
        num_count[num] += 1
        
    for num in num_count:
        if num_count[num] > mode:
            mode = num
    return mode