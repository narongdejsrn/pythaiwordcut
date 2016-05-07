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
def search(word, conn):
    # check latin words
    match = re.search(u"[A-Za-z\d]*", word)
    if match.group(0):
        return match.group(0)

    # check number
    match = re.search(u"[\d]*", word)
    if match.group(0):
        return match.group(0)

    c = conn.cursor()

    longest = 0
    maxData = None

    for data in c.execute("SELECT * FROM dictionary WHERE word LIKE '" + word[0] +"%';"):
        if(len(data[1]) > longest):
            if data[1] in word[0:len(data[1])]:
                longest = len(data[1])
                maxData = data

    if maxData:
        return maxData[1]
    else:
        return -1;

# c = sentence which represent as char
# N = number of character
def find_segment(c, conn):
    i = 0
    N = len(c)
    arr = []
    while(i < N):
        j = search(c[i:N], conn)
        if(j == -1):
            arr.append(c[i])
            i = i + 1
        else:
            arr.append(j)
            i = i + len(j)
        # print ('|', end='')
    return arr;

class wordcut(object):
    def __init__(self):
        self.conn = sqlite3.connect(_DB)

    def segment(self, c):
        return find_segment(c, self.conn)

    def close(self):
        self.conn.close()
