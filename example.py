# -*- coding: utf-8 -*-

import pythaiwordcut as ptw
import time

start_time = time.time()
pt = ptw.wordcut(stopNumber=True, stopDictionary="/Users/zenyai/Documents/Projects/pythaiwordcut/stopword.txt", removeNonCharacter=True, caseSensitive=False, ngram=(1, 1), negation=True, removeRepeat=True)
print "|".join(pt.segment(u'ง่วงงงไม่นอนจังเลยยยยย Test Thai language! 123645 มีผลเรียบเรียงวันที่ 1'))
print("--- %s seconds ---" % (time.time() - start_time))
