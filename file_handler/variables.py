import re
with open('main1.tfc', 'r') as datafile:
    for line in datafile:
        line1=line.strip()
        if '.v' in line1:
            aa = line1
            bb = aa
            bb = bb[3:]
            rt = open('var.py', 'w')
            rt.write(bb+'\n')
            cc = re.split(',', bb)
            asd = len(cc)
            asd1 = str(asd)
            rt.write('number of variables::'+asd1)
            rt.close()
            break
