# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

end_h, end_m = map(int, raw_input().split(':'))
dream_h, dream_m = map(int, raw_input().split(':'))

end = datetime(2000, 7, 7, end_h, end_m)
delta = timedelta(hours=dream_h, minutes=dream_m)

result = (end-delta).time()
print(result.strftime('%H:%M'))
