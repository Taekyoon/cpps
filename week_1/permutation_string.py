def permutation_string(s1, s2):
    """Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
    In other words, one of the first string's permutations is the substring of the second string.

    1. The input strings only contain lower case letters.
    2. The length of both given strings is in range [1, 10,000].

    >>> permutation_string('ab', 'eidbaooo')
    True
    >>> permutation_string('ab', 'eidboaoo')
    False
    >>> permutation_string('abc', 'abc')
    True
    >>> permutation_string('abcde', 'ab')
    False
    >>> permutation_string('abi', 'eidbaoo')
    False
    """
    def check_sub_string_permute(src, tgt):
        src_cnt = {c: 0 for c in set(src)}
        tgt_cnt = {c: 0 for c in set(tgt)}

        for c in src:
            src_cnt[c] += 1
        
        for c in tgt:
            tgt_cnt[c] += 1

        if src_cnt != tgt_cnt:
            return False
        
        return True
    
    if len(s1) > len(s2):
        return False

    num_cand_substr = len(s2) - len(s1) + 1
    sub_str_len = len(s1)

    for i in range(num_cand_substr):
        sub_str = s2[i:i+sub_str_len]
        if check_sub_string_permute(s1, sub_str):
            return True
    
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
