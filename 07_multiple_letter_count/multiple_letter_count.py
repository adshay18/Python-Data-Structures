def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    phrase_set = set(phrase)
    letter_count = dict.fromkeys(phrase_set, 0)
    for char in phrase:
        letter_count[char] += 1
        
    return letter_count