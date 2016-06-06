# -*- coding: utf-8 -*-

#
# based on algorithm from
# http://www.aclweb.org/anthology/E14-4016
#

from __future__ import print_function
import re
import marisa_trie
import os
dir = os.path.dirname(__file__)
_DB_FILE = os.path.join(dir, 'lexitron.txt')

# Find maximum matching in Trie if match return id else return -1
def searchTrie(word, trie):
    # check latin words
    match = re.search(u"[A-Za-z\d]*", word)
    if match.group(0):
        return match.group(0)

    # check number
    match = re.search(u"[\d]*", word)
    if match.group(0):
        return match.group(0)

    longest = 0
    maxData = None

    for data in trie.keys(word[0]):
        if(len(data) > longest):
            if data in word[0:len(data)]:
                longest = len(data)
                maxData = data

    if maxData:
        return maxData
    else:
        return -1;

# c = sentence which represent as char
# N = number of character
def find_segment(c, trie):
    i = 0
    N = len(c)
    arr = []
    while(i < N):
        j = searchTrie(c[i:N], trie)
        if(j == -1):
            arr.append(c[i])
            i = i + 1
        else:
            arr.append(j)
            i = i + len(j)
    return arr;

class wordcut(object):
    def __init__(self):
        d = []
        with open(_DB_FILE) as f:
            for line in f:
                d.append(line.decode('utf-8').rstrip())

        self.trie = marisa_trie.Trie(d)

    def segment(self, c):
        return find_segment(c, self.trie)

    def close(self):
        self.conn.close()
