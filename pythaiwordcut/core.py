# -*- coding: utf-8 -*-

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

# Find in DB if match return id else return -1
def search(word):
    conn = sqlite3.connect(_DB)
    c = conn.cursor()
    c.execute("SELECT id FROM dictionary WHERE word = '%s' LIMIT 1;" % word)
    data = c.fetchone()
    conn.close()
    if data:
        return data[0]
    else:
        return -1;

def segment(c, N, t):
    pass
