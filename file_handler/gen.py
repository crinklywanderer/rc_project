import itertools
outs = open('a.txt', 'w')
a = 2 ** 3
testPatterns = table = list(itertools.product([0,1], repeat=3))
for p in testPatterns:
    a,b,c = p
    b  = a  ^  b
    a = (b and c) ^ a
    b = a  ^  b
    a= not a
    result = [a,b,c]
    for n, i in enumerate(result):
        if i == True:
            result[n]=1
        if i == False:
            result[n]=0
    print(str(p) + ' => ' + str(result))
    outs.write(str(p) + ' => ' + str(result))
    outs.write('\n')

#for io in range(len(result)):
 #   print('Level' + '[' + str(io) + ']')
  #  print(str(p) + '=>' + str(result))
#print("\n")


#    for n, i in enumerate(result):
 #       if i == True:
  #          result[n]=1
   #     if i == False:
    #        result[n]=0
     #   for io in range(len(result)):
      #      print('Level' + '[' + str(io) + ']')
       #     print(str(p) + '=>' + str(result))
        #print("\n")
        #outs.write(str(p) + ' => '+ str(result))
        #outs.write('\n')
#outs.close()







