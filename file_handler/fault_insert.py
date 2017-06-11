alist = []
mo = open('faulty_comp.tfc', 'w')
mo.close()
with open('main1.tfc') as fo:
    for line in fo:
        if line.strip() == 'BEGIN':
            break
    for line in fo:
        if line.strip() == 'END':
            break
        if len(line) == 1:
            if line == '\n':
                continue
        alist.append(line)
print('Enter Level Number To Insert MGF (ONLY NUMBERS ALLOWED)', '\n')
le_no = int(input(''))
with open('main1.tfc') as loo:
    for lp in loo:
        if lp.strip() == 'BEGIN':
            break
        noo = open('faulty_comp.tfc', 'a')
        noo.write(lp)
    noo.write('BEGIN'+'\n')
    for xo in range(len(alist)):
        if alist[xo] == alist[le_no]:
            continue
        noo.write(alist[xo])
    noo.write('END')
