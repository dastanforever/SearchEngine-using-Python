__author__ = 'PranavSharma'

def get_page(url):      # url should be of the form - 'http://www.xyz.com'
    try:
        import urllib2
        source = urllib2.urlopen(url)
        return source.read()
    except:
        print('Error!!!!!!!!!!!!' + url)
        return 'None'

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


def unionlist(a , b):
    for x in b:
        if not x in a:
            a.append(x)
    return a

#def remove_tag(page,s):
#    pos = page.find(s)
#    while pos >= 0:
#        pos2 = page.find('>',pos)
#        page = page[0:pos] + page[pos2+1:]
#        pos = page.find(s)
#    return page


#def remove_string(page,s):
#    pos = page.find(s)
#    s2 = s[0] + '/' + s[1:] + '>'
#    while pos >= 0:
#        pos2 = page.find(s2,pos)
#        pos2 = page.find('>',pos2)
#        page = page[0:pos] + page[pos2+1:]
#        pos = page.find(s)
#    return page

def refine_result(list1):
    res = []
    for q in list1:
        if len(q) > 3 and len(q) < 15:
            res.append(q)
    return res

def get_meta(page):
    pos = page.find('<meta')
    res = ''
    while pos >= 0:
        pos2 = page.find('>',pos)
        res += page[pos:pos2]
        pos = page.find('<meta',pos2)
    res = res.split()
    res2 = []
    for a in res:
        if (not 'meta' in a) and (not '=' in a):
            res2.append(a)
    return refine_result(res2)


#def keep_body(page):
#    pos = page.find('<body')
#    pos = page.find('>',pos)
#    pos2 = page.find('</body>')
#    return page[pos+1:pos2]

def titlePage(page):
    pos = page.find('<title>')
    pos = page.find('>',pos)
    pos2 = page.find('</',pos)
    Title = page[pos+1:pos2]
    return refine_result(Title.split())

def indexer(page):
#    body = keep_body(page)
#    scriptless =  remove_string(body,'<script')
#    styleless = remove_string(scriptless,'<style')
#    tagless = remove_tag(styleless,'<')
#    keywords = tagless.split()
#    keywords = refine_result(keywords)
    meta = get_meta(page)
    title = titlePage(page)
    keywords = unionlist(title,meta)
    return keywords

def update_dic(dic,keywords,url):
    for a in keywords:
        if a in dic:
            dic[a][url] = 1
        else:
            dic[a] = {url:1}
    return dic

def get_main_url(url):
    pos = url.find('htt')
    pos2 = url.find('.',pos)
    pos2 = url.find('.',pos2+1)
    pos2 = url.find('/',pos2)
    if pos2 != -1:
        return url[pos:pos2]
    else:
        return url[pos:]


def diglinks(url,maxpages,depth):   # depth = 1 is ground
    indexed_dic = {}
    tocrawl = [url]
    crawled = []
    num_link_level = 1
    num_link_prev_level = 1
    loop_iterated = 0
    level = 0
    while maxpages > 0 and len(tocrawl) > 0 and depth > level:
        a = tocrawl.pop(0)
        if a not in crawled:
            mainurl = get_main_url(a)
            #print mainurl
            page = get_page(a)
            links = get_all_links(page)
            links2 = []
            for l in links:
                if l[0:3] != 'htt':
                    l = mainurl + l
                    links2.append(l)
                else:
                    links2.append(l)
            #print(links2)
            unionlist(tocrawl,links2)
            crawled.append(a)
            keywords = indexer(page)
            indexed_dic = update_dic(indexed_dic,keywords,a)
            maxpages -= 1
            num_link_level += len(links)
            loop_iterated += 1
            if num_link_prev_level <= loop_iterated:
                level += 1
                loop_iterated = 0
                num_link_prev_level = num_link_level
                num_link_level = 0
    return crawled,indexed_dic

def find_url(keyword,indexed_dic):
    res = {}
    for a in indexed_dic:
        if keyword.lower() in a.lower():
            for b in indexed_dic[a]:
                res[b] = indexed_dic[a][b]
    return res

linkscrawled,index = diglinks('https://www.udacity.com/courses#!/all',4,2000)
print(linkscrawled)
print index
print(find_url('courses',index))



#print get_main_url('http://www.google.com/hjbafhsavf')
#print(get_main_url('http://www.go.co.in/adfbakf/df'))
#print(get_main_url('https://www.udacity.com/courses#!/all'))#

#a = '/courses'
#b = 'http://dasd'
#mainurl = 'google.com'
#a = mainurl + a
#print(a)
#print b[0:3] == 'htt#'