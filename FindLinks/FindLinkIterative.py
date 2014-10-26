__author__ = 'PranavSharma'


def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
        return
    index[keyword] = [url]

def add_page_to_index(index,url,content):
    con = content.split()
    for a in con:
        add_to_index(index,a,url)
    #print con

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


def add_to_index(index,keyword,url):
    for s in index:
        if keyword == s[0]:
            ind = index.index(s)
            index[ind][1].append(url)
            return
    b = [keyword,[url]]
    index.append(b)

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None

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

def compute_ranks(graph):
    d = 0.8 #damping factor
    numloops = 10   #timestep

    ranks = {}
    npages = len(graph)
    for page in graph:          #Initial rank(which is equl to all)
        ranks[page] = 1.0/npages

    for i in range(0,numloops):
        newranks = {}
            for page in graph:
                newrank = (1-d) / npages

            newranks[page] =  newrank
        ranks = newranks
    return ranks




def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl and max_pages>0:
        page = tocrawl.pop()
        if page not in crawled:
            if get_page(page) != 0:
                links = get_all_links(get_page(page))
                graph[page] = links
                union(tocrawl, links)
                add_page_to_index(index,page,get_page(page))
                crawled.append(page)
                max_pages -= 1
    return crawled,graph

#print crawl_web("http://www.udacity.com/cs101x/index.html",1)
#>>> ['http://www.udacity.com/cs101x/index.html']

#print crawl_web("C:\Users\PranavSharma\Desktop\webpage\index.php",2)
#print get_page("http://www.tecnoesis.in")
print crawl_web("http://www.facebook.com",20)
print 'End'
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html']

#print crawl_wb("http://www.udacity.com/cs101x/index.html",500)
#>>> ['http://www.udacity.com/cs101x/index.html',
#>>> 'http://www.udacity.com/cs101x/flying.html',
#>>> 'http://www.udacity.com/cs101x/walking.html',
#>>> 'http://www.udacity.com/cs101x/crawling.html',
#>>> 'http://www.udacity.com/cs101x/kicking.html']

