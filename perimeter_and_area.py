#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This is the "Perimeter and Area" program


def main():
    print('If a rectangle has dimensions:')
    print('5cm x 3cm')
    print('')
    print('The area is {}cm\u00b2'.format(5 * 3))
    # I learned \u00b2 from (continued)
    # https://stackoverflow.com/questions/ (continued)
    # 8651361/how-do-you-print-superscript-in-python
    print('The perimeter is {}cm'.format(2 * (5 + 3)))


if __name__ == "__main__":
    main()
