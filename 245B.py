# -*- coding: utf-8 -*-
import re

pattern = re.compile('(http|ftp)(?!(ru)\w+)', re.DOTALL)

# result = pattern.findall(raw_input())
# result = pattern.match('httpuururrururruruurururrrrrurrurrurruruuruuu')
result = pattern.findall('ftphttprururu')
# result = pattern.findall('httpuururrururruruurururrrrrurrurrurruruuruuu')
print(result)
# print re
# if result:
#     print(result.groups())
# result = result[0]
# if len(result) == 4:
#     print('{}://{}.{}/{}'.format(*result))
# else:
#     print('{}://{}.{}'.format(*result))
