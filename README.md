Map-Reduce: Words per Author
============================

Introduction
------------

Map-Reduce experiment to count words in book title per author stored in multiple files.

Written in python using the map-reduce lightweight implementation [mincemeat.py](https://raw.github.com/michaelfairley/mincemeatpy/master/mincemeat.py) 

This is an exercise proposed in the [Web Intelligence and Big Data course in Coursera.org](https://class.coursera.org/bigdata-002/class/index)


Problem description
-------------------

There are some files containing entries that look like:

```bash
journals/cl/SantoNR90:::Michele Di Santo::Libero Nigro::Wilma Russo:::Programmer-Defined Control Abstractions in Modula-2.
```

that represent bibliographic information about publications, formatted as follows:

```bash
paper-id:::author1::author2::…. ::authorN:::title
```

The task is to compute how many times every term occurs across titles, for each author.

For example, the author Alberto Pettorossi the following terms occur in titles with the indicated cumulative frequencies (across all his papers): program:3, transformation:2, transforming:2, using:2, programs:2, and logic:2.

Remember that an author might have written multiple papers, which might be listed in multiple files. Further notice that ‘terms’ must exclude common stop-words, such as prepositions etc. For the purpose of this assignment, the stop-words that need to be omitted are listed in the script stopwords.py. In addition, single letter words, such as "a" can be ignored; also hyphens can be ignored (i.e. deleted). Lastly, periods, commas, etc. need to be ignored; in other words, only alphabets and numbers can be part of a title term: Thus, “program” and “program.” should both be counted as the term ‘program’, and "map-reduce" should be taken as 'map reduce'. Note: You do not need to do stemming, i.e. "algorithm" and "algorithms" can be treated as separate terms.

The assignment is to write a parallel map-reduce program for the above task using either octo.py, or mincemeat.py, each of which is a lightweight map-reduce implementation written in Python.

