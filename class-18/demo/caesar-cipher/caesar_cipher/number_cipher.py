def encrypt(number, key):
    """
    number: integer to be encrypted
    key: number of times we shift

    return an encrypted integer

    >>> encrypt(1234, 2)
    3456

    >>> encrypt(3246, 1)
    4357
    """

    numer_as_str = str(number)
    result = ''
    # '1234'
    # for each digit in the string:
    #   convert to integer
    #   shift it (adding the key to it)
    #   put back to the string using concatenation

    # if key > 10:
    #     key -= 10

    for char in numer_as_str:
        num = int(char)
        num += key
        num = num % 10
        result += str(num)

    return int(result)


def decrypt(number, key):
    return encrypt(number, -key)


if __name__ == "__main__":
    assert encrypt(1234, 2) == 3456
    assert encrypt(3246, 1) == 4357
    # assert encrypt(4357, -1) == 3246
    assert decrypt(4357, 1) == 3246
    assert encrypt(123, 15) == 678
    print('All tests passed!!!!')

# digits = ['3','4','5','6']
# '3456'
# ''.join(digits)

