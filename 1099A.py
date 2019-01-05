w, h = map(int, raw_input().split())
u_1, d_1 = map(int, raw_input().split())
u_2, d_2 = map(int, raw_input().split())

r = w

for i in xrange(h, -1, -1):
	r += i
	if i == d_1:
		r = max(r-u_1, 0)
	elif i == d_2:
		r = max(r-u_2, 0)
print(r)