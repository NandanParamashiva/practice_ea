#!/usr/bin/python

def test_f(test_dict):
    test_dict[10] = 'ten'
    test_dict[20] = 'twenty'

def func(local):
    local.append(1)
    local.append(55)

def main():
    print 'hey'

    var = []
    func(var)
    print var

    test = {}
    test_f(test)
    print test

if __name__ == '__main__':
    main()