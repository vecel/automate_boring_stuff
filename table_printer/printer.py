
example_table = [
    ['cat', 'dog', 'snake'],
    ['dinosaur', 'snail', 'bird'],
    ['owl', '-', 'bug', 'something'],
    ['something'],
]

def print_2dim_table(table: list, character: str = '.') -> int:
    ''' Print nicely given 2-dimensional list.
        Return width of printed elements (including centering characters)
    
        Assume, that each inner list contains same number of element.'''

    width = 0
    max_list_len = 0
    for row in table:
        max_list_len = max(max_list_len, len(row))
        for elem in row:
            width = max(width, len(elem))
    
    width += 2

    for row in table:
        for i in range(max_list_len - len(row)):
            row.append('-')
        for elem in row:
            print(elem.center(width, character), end = ' ')
        print()
    return width
