# -*- coding: utf-8 -*-

#
# based on algorithm from
# http://www.aclweb.org/anthology/E14-4016
#

from __future__ import print_function
import sqlite3
import re


import os
dir = os.path.dirname(__file__)
_DB = os.path.join(dir, 'dictionary.original.db')

def importToDictionary(filename):
    conn = sqlite3.connect(_DB)
    c = conn.cursor()
    with open(filename) as f:
        lines = f.read().splitlines()

    for l in lines:
        c.execute("INSERT INTO dictionary ('word') VALUES ('%s')" % l)
        conn.commit()

    conn.close()

# Find maximum matching in DB if match return id else return -1
def search(word):

    # check latin words
    match = re.search(u"[A-Za-z\d]*", word)
    if match.group(0):
        return match.group(0)

    # check number
    match = re.search(u"[\d]*", word)
    if match.group(0):
        return match.group(0)


    conn = sqlite3.connect(_DB)
    c = conn.cursor()

    longest = 0
    maxData = None
    for data in c.execute("SELECT * FROM dictionary WHERE word LIKE '" + word[0] +"%';"):
        if(len(data[1]) > longest):
            if data[1] in word[0:len(data[1])]:
                longest = len(data[1])
                maxData = data

    conn.close()
    if maxData:
        return maxData[1]
    else:
        return -1;

# c = sentence which represent as char
# N = number of character
def segment(c):
    i = 0
    N = len(c)
    while(i < N):
        j = search(c[i:N])
        if(j == -1):
            print (c[i], end='')
            i = i + 1
        else:
            print (j, end='')
            i = i + len(j)
        print ('|', end='')
    print()
