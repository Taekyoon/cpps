def rotate_string(s1, s2):
    """
    >>> rotate_string('abcde', 'cdeab')
    True
    >>> rotate_string('abcde', 'cdeac')
    False
    >>> rotate_string('aba', 'aab')
    True
    >>> rotate_string('aaa', 'a')
    False
    """
    # kmp case
    if len(s1) !=len(s2):
        return False

    if s1 == s2:
        return True

    s1 = s1 * 2
    id2 = 0

    for i in range(len(s1)):
        if id2 >= len(s2):
            return True
        if s1[i] == s2[id2]:
            id2 += 1
        else:
            id2 = 0

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
