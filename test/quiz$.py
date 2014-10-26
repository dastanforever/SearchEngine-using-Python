# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    con = content.split()
    for a in con:
        add_to_index(index,a,url)
    #print con

def add_to_index2(index, keyword, url):
    index.append([keyword, url])

def lookup(index, keyword):
    result = []
    for entry in index:
        if entry[0] == keyword:
            result.append(entry[1])
    return result



add_page_to_index(index,'fake.text',"This is a test")
add_page_to_index(index,'real.text',"This is not a test")
print index
print index[1]
print index[4]
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


