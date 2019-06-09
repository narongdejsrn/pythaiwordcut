# -*- coding: utf-8 -*-

import pythaiwordcut as ptw
import time

start_time = time.time()
pt = ptw.wordcut(stopNumber=False, removeNonCharacter=True, caseSensitive=False, ngram=(1, 1), negation=True, removeRepeat=True)
print("|".join(pt.segment(u'ง่วงงงไม่นอนจังเลยยยยย Test Thai language! 123645 แต่มีผลเรียบเรียงวันที่ 1')))
print("--- %s seconds ---" % (time.time() - start_time))
