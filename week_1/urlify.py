def urlify(s):
    """Write a method to replace all the spaces in a string S with ‘%20’. 
    You may assume that the string has sufficient space (or allocated memory) at the end to hold the additional characters,
    Note: The leading and trailing spaces should be trimmed off and not replaced by %20.

    Input:
    The first line contains a string S. 

    Output:
    For each testcase, in a new line, print the string with spaces replaced by "%20".

    >>> urlify('Mr John Smith')
    'Mr%20John%20Smith'
    >>> urlify('Mr Benedict Cumberbatch  ')
    'Mr%20Benedict%20Cumberbatch'
    """

    return s.strip().replace(' ', '%20')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
