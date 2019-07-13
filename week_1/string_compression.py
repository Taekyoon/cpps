def string_compression(s):
    """
    >>> string_compression('aabcccccaaa')
    'a2b1c5a3'
    >>> string_compression('abcdef')
    'a1b1c1d1e1f1'
    """
    out_s = ''
    cnt = 1

    for i, c in enumerate(s[:-1]):
        if s[i] != s[i+1]:
            out_s += '{}{}'.format(c, cnt)
            cnt = 0
        cnt += 1
    
    out_s += '{}{}'.format(s[-1], cnt)
    
    return out_s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
