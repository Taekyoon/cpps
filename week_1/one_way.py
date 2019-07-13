def one_way(s1, s2):
    """There are three types of edits that can be performed on strings: 
    insert a character, remove a character, or replace a character. 
    Given two strings, write a function to check if they are one edit (or zero edits) away.

    >>> one_way('pale', 'ple')
    True
    >>> one_way('pales', 'pale')
    True
    >>> one_way('pale', 'bale')
    True
    >>> one_way('pale', 'bake')
    False
    """
    if len(s1) == len(s2):
        diff = 0
        for c1, c2 in zip(s1, s2):
            if diff > 1:
                return False
            if c1 != c2:
                diff += 1
        if diff > 1:
            return False
        return True
    elif len(s1) != len(s2):
        if abs(len(s1) - len(s2)) > 1:
            return False

        min_len = min([len(s1), len(s2)])

        id1, id2 = 0, 0
        act = 0
        while id1 < min_len and id2 < min_len:
            if act > 1:
                return False
            if s1[id1] == s2[id2]:
                id1 += 1
                id2 += 1
            else:
                if s1[id1 + 1] == s2[id2]:
                    act += 1
                    id1 += 1
                else:
                    act += 1
                    id1 += 1
                    id2 += 1
        if act > 1:
            return False
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
