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

    # new_s += '{}_{} '.format(s[0], id)

    # for i, c in enumerate(s[1:-1]):
    #     if s[i] != s[i+1]:
    #         id += 1            
    #     new_s += '{}_{} '.format(c, id)

    # if s[-2] != s[-1]:
    #     id += 1
    # new_s += '{}_{} '.format(c, id)

    # unique_elements = set(new_s.split())
    # cnt_elements = {e: 0 for e in unique_elements}

    # for e in new_s.split():
    #     cnt_elements[e] += 1

    # sorted_cnt_elements = sorted(cnt_elements.items(), key=lambda x: int(x.split('_')[-1]))

    # for s_e in sorted_cnt_elements:
    #     out_s += '{}{}'.format(s_e.split('_')[0], sorted_cnt_elements[s_e])
    
    return out_s


if __name__ == "__main__":
    import doctest
    doctest.testmod()
