def unique_chars(s):
    """Implement an algorithm to determine if a string has all unique characters. 
    The program should only check if alphabetic characters are unique. Spaces, quotations, numbers, etc should be ignored. 
    The case of each character matters. 'A' is not the same as 'a'.

    The input is one line containing any number of characters.
    
    The output should be either "Yes" or "No" with no spaces.

    >>> unique_chars('abcde')
    'Yes'
    >>> unique_chars('aaaaa')
    'No'
    """
    s_cnt = {c: 0 for c in set(s)}

    for c in s:
        s_cnt[c] += 1
        if s_cnt[c] > 1:
            return 'No'

    return 'Yes'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
