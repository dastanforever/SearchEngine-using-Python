__author__ = 'PranavSharma'

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    res = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            res.append(url)
            page = page[endpos:]
        else:
            break
    return res

def get_page(page):
    try:
        import urllib2
        source = urllib2.urlopen(page)
        return source.read()
    except:
        print('Error!!!!!!!!!!!!')
        return 0

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url,end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            if str(url)[0:3]=='htt':
                print(url)
                links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl and max_pages>0:
        page = tocrawl.pop()
        if page not in crawled:
            if get_page(page) != 0:
                union(tocrawl, get_all_links(get_page(page)))
                crawled.append(page)
                max_pages -= 1
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html']

#print crawl_web("C:\Users\PranavSharma\Desktop\webpage\index.php",2)
#print get_page("http://www.tecnoesis.in")
print crawl_web("http://www.tecnoesis.in",10)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html']

print crawl_web("http://www.udacity.com/cs101x/index.html",500)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']