#!/usr/bin/env python3

'''
Purpose ▶︎▶︎ TODO What does this script do?
Copyright by SuperUdo3000, June 2022
Version: 0.2
'''


def main(first_arg):
    ''' ▶︎▶︎ TODO What does this function do? '''

    # . ▶︎▶︎ TODO REPLACE THIS WITH YOUR AWESOME CODE

    return


if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser(
            description=sys.modules['__main__'].__doc__,
            formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('first_arg', nargs='?', help='▶︎▶︎ TODO')

    args = parser.parse_args()
    main(args.first_arg)

else:
    import os.path
    print(os.path.basename(__file__), 'imported.')


# ADDITIONAL STUFF

# def testing():
#     '''▶︎▶︎ TODO Test all your functions'''
#     assert(main(None) == None)
#     assert(your_method(you_argument) == 'Result Expected')

# Hint: using doc string as description, formatter preserves line breaks.
# Quick Start: python3 TEMPLATE.py -h
#   this will show a help text based on the doc string at the very top.
