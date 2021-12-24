def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_list = []
    for char in phrase:
        if char.lower() in 'aeiou':
            vowel_list.append(char.lower())
    vowel_set = set(vowel_list)
    vowel_dict = dict.fromkeys(vowel_set, 0)
    for vowel in vowel_list:
        if vowel in vowel_set:
            vowel_dict[vowel] += 1
            
    return vowel_dict