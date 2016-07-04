# -*- coding:utf-8 -*-
import re
pattern1 = r'^\d{3}\-\d{3,8}$'
print('正则',pattern1)
if re.match(pattern1, '010-12345'):
    print('ok')
else:
    print('failed')
    
res1 = re.match(pattern1, '010 12345')
print('010 12345', res1)


