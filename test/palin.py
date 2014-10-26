__author__ = 'PranavSharma'

def is_palindrome(a):
    if len(a) <= 1:
        return True
    else:
        if a[0] == a[len(a)-1]:
            a = a[1:len(a)-1]
            return (is_palindrome(a))
        else:
            return False

print(is_palindrome('d'))
print(is_palindrome(''))
print(is_palindrome('abcd'))
print(is_palindrome('abba'))
print(len('aba'))
b = 'aba'
print(b[1:3])
