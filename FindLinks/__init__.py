__author__ = 'PranavSharma'

def get_next_target(page):
    start_link = page.find('src=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url,endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

def get_page(page):
    import urllib2
    source = urllib2.urlopen(page)
    return source.read()
print_all_links('<a href="asdasdasd" sjkadnlaksd fkdsfsdjf')
print_all_links(get_page("http://www.microsoft.com/en/us/default.aspx?redir=true"))