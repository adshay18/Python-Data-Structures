def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = list(str(num1))
    num1_set = set(list(str(num1)))
    num1_dict = dict.fromkeys(num1_set, 0)
    
    for num in num1_list:
        num1_dict[num] += 1
    
    num2_list = list(str(num2))
    num2_set = set(list(str(num2)))
    num2_dict = dict.fromkeys(num2_set, 0)
    
    for num in num2_list:
        num2_dict[num] += 1
    
    if num1_dict == num2_dict:
        return True
    return False