__author__ = 'PranavSharma'

def unionlist(a , b):
    for x in b:
        if not x in a:
            a.append(x)
    return a

def get_page(url):      # url should be of the form - 'http://www.xyz.com'
    try:
        import urllib2
        source = urllib2.urlopen(url)
        return source.read()
    except:
        print('Invalid Url')
        return 0

def remove_tag(page,s):
    pos = page.find(s)
    while pos >= 0:
        pos2 = page.find('>',pos)
        page = page[0:pos] + page[pos2+1:]
        pos = page.find(s)
    return page


def remove_string(page,s):
    pos = page.find(s)
    s2 = s[0] + '/' + s[1:] + '>'
    while pos >= 0:
        pos2 = page.find(s2,pos)
        pos2 = page.find('>',pos2)
        page = page[0:pos] + page[pos2+1:]
        pos = page.find(s)
    return page

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


def keep_body(page):
    pos = page.find('<body')
    pos = page.find('>',pos)
    pos2 = page.find('</body>')
    return page[pos+1:pos2]

def titlePage(page):
    pos = page.find('<title>')
    pos = page.find('>',pos)
    pos2 = page.find('</',pos)
    Title = page[pos+1:pos2]
    return refine_result(Title.split())


page = get_page('http://www.outlook.com')
body = keep_body(page)
scriptless =  remove_string(body,'<script')
styleless = remove_string(scriptless,'<style')
tagless = remove_tag(styleless,'<')
keywords = tagless.split()
keywords = refine_result(keywords)
meta = get_meta(page)
title = titlePage(page)
print(title)
keywords = unionlist(unionlist(title,meta),keywords)
print(keywords)