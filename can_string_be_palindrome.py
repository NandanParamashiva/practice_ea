#! /usr/bin/python


def can_string_be_palindrome(str):
    map = {}
    for i in xrange(len(str)):
        char = str[i]
        if not map.has_key(char):
            map[char] = 0
        map[char] += 1

    if len(str) % 2 == 0 :
        #even
        allowed_odd = 0
    else:
        allowed_odd = 1

    for key in map:
        if map[key] % 2 == 0:
            continue
        else:
            allowed_odd -= 1
            if allowed_odd < 0:
                print 'not palindromic'
                return 0
    print 'is palindromic'
    return 1

def main():
    str = 'edifftttiied'
    res = can_string_be_palindrome(str)
    print res


if __name__ == '__main__':
    main()
