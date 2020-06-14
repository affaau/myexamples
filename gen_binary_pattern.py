from pprint import pprint
import sys


def bin_pattern(N):
    '''N is number of binary digit to display
    - fills with 0
    '''
    if int(N) < 0:
        print('Error:: Only positive integer allowed!')
        sys.exit()

    fmt = '{:0' + str(int(N)) + 'b}'
    binary_format_lst = [fmt.format(e) for e in range(2**N)]
    return binary_format_lst


if __name__ == '__main__':
    result = bin_pattern(5)
    # Apply PrettyPrint if output len>2
    pprint(result, width=2)
