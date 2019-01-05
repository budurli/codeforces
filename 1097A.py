card = raw_input()
cards = raw_input().split()

m = [x[0] for x in cards]
r = [r[1] for r in cards]

if card[0] in m or card[1] in r:
    print('YES') 
else:
	print('NO')