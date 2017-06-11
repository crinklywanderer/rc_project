import re

graph_list = []
a_list = []
a = open('resultant_image.py', 'w')
a.close()

with open('/home/aayush/Desktop/Mini-project/work/file_handler/quasm/qasm2circ-v1.4/converted_image.real', 'r') as file:
    for line in file:
        if line.strip() == '.begin':
            break
        graph_list.append(line)
    for line in file:
        if line.strip() == '.end':
            break
        a_list.append(line)


print('graph list', graph_list)
print('a_list', a_list)
for i in range(len(graph_list)):
    var1 = str(graph_list[i])
    if 'inputs' in var1:
        var1 = re.split('\\s', var1)
        del var1[0]; del var1[-1]; del var1[-1]
        for ii in range(len(var1)):
            with open('resultant_image.py', 'a') as lex:
                lex.write(str(var1[ii]))
        print('yes', var1)