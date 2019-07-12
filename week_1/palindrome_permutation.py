def palindrome_permutation(s):
    """Complete the gameOfThrones function below to determine whether a given string can be rearranged into a palindrome. 
    If it is possible, return YES, otherwise return NO.

    Input Format:
    A single line which contains , the input string.

    Output Format:
    A single line which contains YES or NO.

    >>> palindrome_permutation('aaabbbb')
    'Yes'
    >>> palindrome_permutation('cdefghmnopqrstuvw')
    'No'
    >>> palindrome_permutation('cdcdcdcdeeeef')
    'Yes'
    """
    s_cnt = {c: 0 for c in set(s)}
    has_single = False

    for c in s:
        s_cnt[c] += 1
    
    for c in s_cnt:
        if s_cnt[c] % 2 == 1:
            if has_single:
                return 'No'
            else:
                has_single = True
    
    return 'Yes'

if __name__ == "__main__":
    import doctest
    doctest.testmod()