# -*- coding: utf-8 -*-
import operator
n, k = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
b = map(int, raw_input().split(' '))

result = []
for i in xrange(n / k):
    should_not_count = ((b[i]+1) * 10 ** (k-1) - 1) / a[i] - (b[i] * 10 ** (k-1)-1) / a[i]
    print(((b[i]+1) * 10 ** (k-1) - 1) / a[i], (b[i] * 10 ** (k-1)-1) / a[i])
    result.append((10**k-1) / a[i] + 1 - should_not_count)

print(reduce(operator.mul, result, 1))