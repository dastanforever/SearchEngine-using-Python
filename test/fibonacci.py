__author__ = 'PranavSharma'

def f(n):
    if n<=1:
        if n == 0:
            return 0
        else:
            return 1
    else:
        return f(n-1)+f(n-2)
