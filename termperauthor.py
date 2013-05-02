#!/usr/bin/env python
import mincemeat
import glob
import pprint

text_files = glob.glob('hw3data/*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
                for file_name in text_files)




# This processes each file and generates a map of authors mapped to another map of words found in a given document.
# Therefore you'll probably find more than one map of words (one per document) for a given author.
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
            w = w.replace('.','')
            print
            print "word: "+w

            if len(w)>1 and w not in stopwords.allStopWords.keys():
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

# Gets the multiple maps of words (vs) per author (k) (vs) and adds them up to generate a single map of words per author
# In other words, it reduces multiple maps of words found in diferent files for a given author to a single map of wors per author 
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
pprint.pprint(results)

