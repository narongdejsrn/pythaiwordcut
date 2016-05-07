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

def wordcut(sentence):
    conn = sqlite3.connect(_DB)
    c = conn.cursor()
    for data in c.execute("SELECT * FROM dictionary WHERE word LIKE '" + sentence + "%';"):
        print data
    conn.close()
