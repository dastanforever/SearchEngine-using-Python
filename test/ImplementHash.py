__author__ = 'PranavSharma'


def make_hash_table(n):
    hash_table = []
    for i in range(0,n):
        hash_table.append([])
    return hash_table

def hash_string(keyword,nbuckets):
    res = 0
    for c in keyword:
        res = (res + ord(c)) % nbuckets
    return res

def hash_table_get_bucket(hashtable,keyword):
    return hash_string(keyword,len(hashtable))

def hashtable_add(htable,key,value):
    a = hash_table_get_bucket(htable,key)
    for b in a:
        if key == b[0]:
            b[1].append(value)
            return htable
    a.append([key,[value]])
    return htable


print make_hash_table(4)