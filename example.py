# -*- coding: utf-8 -*-

import pythaiwordcut as ptw
import time

start_time = time.time()
pt = ptw.wordcut(stopNumber=True)
print "|".join(pt.segment(u'ง่วงงงนอนจังเลยยยยย 123645'))
print("--- %s seconds ---" % (time.time() - start_time))
