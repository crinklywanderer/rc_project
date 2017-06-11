#from more_itertools import unique_everseen
#import itertools
#import re
#mid_list = list()
#op_list = list()
#check_list = list()
#check_list1 = list()
#aloo = list()
#def checker(liter):
 #   for im in range(len(liter)):
  #      print (liter[im])
   #     af = str(liter[im])
    #    mid_list = af
     #   for xx in range(len(mid_list)):
      #      nn = len(mid_list) - 1
       #     for ro in range(len(mid_list)):
        #        if mid_list[ro] == mid_list[xx]:
         #           continue
          #      else:
           #         print ('This vector can check between Line : ' + str(xx) + ' and ' + str(ro))
            #        alp = str(xx) +  str(ro)
             #       check_list.append(alp)

#    check_list1 = list(unique_everseen(check_list))
 #   print ('\n')
  #  return check_list1

#def invert(item):
#    d = list()
 #   for k in range(len(item)):
#
 #       copy = list(item[k])
  #      for l in range(len(copy)):
   #         if copy[l] == str(1):
    #            copy[l] = str(0)
     #           continue
      #      if copy[l] == str(0):
       #         copy[l] = str(1)
        #copy = ''.join(copy)
        #d.append(copy)
    #for k in range(len(d)):
     #   if d[k] in item:
      #      item.remove(d[k])
    #return item

#def main_fun(aalist):
 #   mid_list1=list()
  #  for ins in range(len(aalist)):
   #     op_list = str(aalist[ins])
    #    var1 = op_list+'0'
     #   var2 = op_list+'1'
      #  mid_list1.append(var1)
       # mid_list1.append(var2)
    #return list(unique_everseen(mid_list1))

#alist = ['01']
#inu = int(input('ENTER NUMBER OF MORE LINES YOU WANT TO MANIPULATE'))

#if inu > 2:
 #   for amy in range(3,inu+1):
  #      alist = main_fun(alist)
   #     check_list1 = checker(alist)

#for ipo in range(0,inu):
 #   aloo.append(ipo)
#aloo = list(itertools.permutations(aloo, 2))

#for iii in range(len(aloo)):
 #   var1 = str(aloo[iii][0])
  #  for jjj in range(1,len(aloo[iii])):
   #     var1 += str(aloo[iii][jjj])
    #aloo[iii] = var1
#check_list1.sort()
#aloo.sort()
#print (str(check_list1) == str(aloo))
#print (alist)
#alist = invert(alist)
#print (check_list1)
#print (aloo)


from more_itertools import unique_everseen
import itertools
import re
mid_list = list()
op_list = list()
test=[]
check_list1 = list()
aloo = list()
def checker(liter,lit):
    check_list = list()
    #print ('this is current value of liter ', liter)
    for im in range(len(liter)):
        #print ('-------------------------------------------------------------')
        #print (liter[im])
        af = str(liter[im])
        mid_list = af
        for xx in range(len(mid_list)):
            nn = len(mid_list) - 1
            for ro in range(len(mid_list)):
                if mid_list[ro] == mid_list[xx]:
                    continue
                else:
                    #print ('This vector can check between Line : ' + str(xx) + ' and ' + str(ro))
                    alp = str(xx) +  str(ro)
                    check_list.append(alp)
    check_list1 = list(unique_everseen(check_list))
    check_list1.sort()
    #print ('inside function', check_list1)
    #print (lit)
    #print ('\n')
    return check_list1


def invert(item):
    d = list()
    for k in range(len(item)):

        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    for k in range(len(d)):
        if d[k] in item:
            item.remove(d[k])
    return item

def invertq(item):
    d = list()
    for k in range(len(item)):

        copy = list(item[k])
        for l in range(len(copy)):
            if copy[l] == str(1):
                copy[l] = str(0)
                continue
            if copy[l] == str(0):
                copy[l] = str(1)
        copy = ''.join(copy)
        d.append(copy)
    d=''.join(d)
    return d




def main_fun(aalist):
    mid_list1=list()
    for ins in range(len(aalist)):
        op_list = str(aalist[ins])
        var1 = op_list+'0'
        var2 = op_list+'1'
        mid_list1.append(var1)
        mid_list1.append(var2)
    return list(unique_everseen(mid_list1))

alist = ['01']
inu = int(input('ENTER NUMBER OF MORE LINES YOU WANT TO MANIPULATE'))

if inu > 2:
    for amy in range(3,inu+1):
        alist = main_fun(alist)
        #check_list1 = checker(alist)

for ipo in range(0,inu):
    aloo.append(ipo)
aloo = list(itertools.permutations(aloo, 2))
aloo.sort()

for iii in range(len(aloo)):
    var1 = str(aloo[iii][0])
    for jjj in range(1,len(aloo[iii])):
        var1 += str(aloo[iii][jjj])
    aloo[iii] = var1
check_list1.sort()
aloo.sort()
#print (str(check_list1) == str(aloo))
#print (alist)
alist = invert(alist)
#print ('this is aloo', aloo)
combs = []
for qw in xrange(1 , len(alist) + 1):
    els = [list(x) for x in itertools.combinations(alist , qw)]
    combs.extend(els)
for qwe in range(len(combs)):
    amp = checker(combs[qwe],aloo)
    if str(amp)==str(aloo):
        print 'Test Pattern for Bridging fault',combs[qwe]
        test=combs[qwe]

        break
news=invertq(test[0])
test.append(news)
print 'Test Pattern for Stuck-at-Fault',test