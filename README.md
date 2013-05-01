Map-Reduce: Words per Author
============================

Introduction
------------

Map-Reduce experiment to count words in book title per author stored in multiple files.

Written in python using the map-reduce lightweight implementation [mincemeat.py](https://raw.github.com/michaelfairley/mincemeatpy/master/mincemeat.py) 


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

