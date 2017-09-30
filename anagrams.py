
def anagrams(words, map):
    for word in words:
        #print word.lower()
        l = sorted(word)
        sorted_word = ''.join(l)
        if not map.has_key(sorted_word):
            map[sorted_word] = []
        map[sorted_word].append(word) #adding to map
    print 'map=',map

def display(map):
    for i in map:
        print map[i] # accessing elem in map

'''def clear(map):

    #print map

    #print map.iteritems()

    keys = map.keys()
    print 'keys=', keys

    #print map.get(keys[0])

    #print 'items =',map.items()

    print 'start loop'
    for k, v in map.iteritems():
        #print k,v
        if k == ''.join(sorted('debitcard')):
            #break
            del map[k]
    #del map[k]
    print 'here='
    keys = map.keys()
    print 'keys=', keys

    for i in dict(map):
        map = del map[i]
    print 'cleared=',dictionary'''

def main():
    words = ['debitcard', 'elvis', 'silent', 'badcredit', 'lives', 'freedom','listen', 'levis', 'money']
    ana_map = {}
    anagrams(words, ana_map)
    #display(ana_map)
    #clear(ana_map)
    print 'ana=',ana_map
    del(ana_map)
    print 'ana2=', ana_map
    #print result


if __name__=='__main__':
    main()