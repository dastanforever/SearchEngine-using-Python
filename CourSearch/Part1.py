__author__ = 'PranavSharma'

def get_page(url):      # url should be of the form - 'http://www.xyz.com'
    try:
        import urllib2
        source = urllib2.urlopen(url)
        return source.read()
    except:
        print('Error!!!!!!!!!!!!')
        return 0

def get_next_link(page,startpos):
    pos = page.find('<a href=',startpos)
    pos = page.find('"',pos+1)
    endpos = page.find('"',pos + 1)
    link = page[pos+1:endpos]
    return link,endpos+1



def if_next_link(page,startpos):
    ans = page.find('<a href=',startpos)
    if ans == -1:
        return False
    return True


def get_all_links(page):
    res = []
    startpos = 0
    while if_next_link(page,startpos):
        current_link,startpos = get_next_link(page,startpos)
        res.append(current_link)
    return res



print get_all_links(get_page('http://www.google.com'))