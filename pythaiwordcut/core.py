# -*- coding: utf-8 -*-
from __future__ import print_function
import sqlite3

_DB = 'pythaiwordcut/dictionary.original.db'

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
    conn = sqlite3.connect(_DB)
    c = conn.cursor()

    longest = 0
    maxData = None
    for data in c.execute("SELECT * FROM dictionary WHERE word LIKE '" + word[0] +"%';"):
        if(len(data[1]) > longest):
            if data[1] in word:
                longest = len(data[1])
                maxData = data

    conn.close()
    if maxData:
        return maxData
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
            print (j[1], end='')
            i = i + len(j[1])
        print ('|', end='')
