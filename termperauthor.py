#!/usr/bin/env python
import mincemeat
import glob
#import stopwords

text_files = glob.glob('small/*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
                for file_name in text_files)

def mapfn(k, v):
    authors_in_doc = {}

    for line in v.splitlines():
        tokens = line.split(':::')
        paperid = tokens[0]
        authors_str = tokens[1]
        authors = authors_str.split('::')
        title = tokens[2]

        for word in title.split():
            w = word.lower()
            print
            print "word: "+w
            
            for author in authors:
                if author not in authors_in_doc.keys():
                    print "author: "+author
                    authors_in_doc[author] = {}

                for w2 in authors_in_doc[author].keys():
                    print "authors_in_doc["+author+"]: " + w2

                
                if w in authors_in_doc[author].keys():
                    print "adding up word in "+author+": "+w
                    authors_in_doc[author][w] = authors_in_doc[author][w]+1
                else:
                    print "new word in "+author+": "+w
                    authors_in_doc[author][w] = 1

    for author in authors_in_doc.keys():
        yield author, authors_in_doc[author]

def reducefn(k, vs):
    words_sum = {}

    for words_in_doc in vs:
        for word in words_in_doc.keys():
            if word in words_sum.keys():
                words_sum[word] = words_sum[word] + words_in_doc[word]
            else:
                words_sum[word] = words_in_doc[word]
                
    return k, words_sum

s = mincemeat.Server()

# The data source can be any dictionary-like object
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results