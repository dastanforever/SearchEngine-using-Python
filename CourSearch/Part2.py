__author__ = 'PranavSharma'

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
        if current_link[0:4] == 'http':
            res.append(current_link)
    return res


def unionlist(a , b):
    for x in b:
        if not x in a:
            a.append(x)
    return a

def diglinks(url,maxpages,depth):   # depth = 1 is ground
    tocrawl = [url]
    crawled = []
    num_link_level = 1
    num_link_prev_level = 1
    loop_iterated = 0
    level = 0
    while maxpages > 0 and len(tocrawl) > 0 and depth > level:
        a = tocrawl.pop(0)
        page = get_page(a)
        links = get_all_links(page)
        unionlist(tocrawl,links)
        crawled.append(a)
        maxpages -= 1
        num_link_level += len(links)
        loop_iterated += 1
        if num_link_prev_level <= loop_iterated:
            level += 1
            loop_iterated = 0
            num_link_prev_level = num_link_level
            num_link_level = 0
    return crawled

print(diglinks('http://www.tecnoesis.in',20,3))
