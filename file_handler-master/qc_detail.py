import re

gate_list = []
gate_list_temp = []
gate_sublist = []

with open('/home/aayush/Desktop/Mini-project/work/file_handler/quasm/qasm2circ-v1.4/converted_image.real', 'r+') as file:
    for line in file:
        if line.strip() == '.begin':
            break
    for line in file:
        if line.strip() == '.end':
            break
        gate_list.append(line)

# print('gates', gate_list)
for i in range(len(gate_list)):
    gate_sublist = (gate_list[i])
    gate_sublist = re.split('\\s', gate_sublist)
    del gate_sublist[-1]
    gate_list_temp.append(gate_sublist)
    # print('gate_sublist', gate_sublist)

print('gate list temp==', gate_list_temp)

for ii in range(len(gate_list_temp)):
    alpha = gate_list_temp[ii]
    # print('alpha', alpha)
    if len(alpha) == 2:
        d1 = alpha[0]
        if len(d1) == 1:
            if d1 == 'v':
                var1 = alpha
                print('gate type - v , ', 'control variable = 0 , target variable = 1', var1[-1], ', Level-', ii, '\n')

        if len(d1) == 2:
            if d1[0] == 'v' and d1[1] == '+':
                var2 = alpha
                print('gate type - v+ , ', 'control variable = 0 , target variable = ', var2[-1], ', Level-', ii, '\n')

            if (d1[0] == 't' and d1[1] == '1') or (d1[0] == 'T' and d1[1] == '1'):
                var3 = alpha
                print('gate type - not , ', 'control variable = 0 , target variable = 1', var3[-1], ', Level-', ii, '\n')

    if len(alpha) == 3:
        d2 = alpha[0]
        if len(d2) == 1:
            if d2[0] == 'v':
                e1 = alpha
                print('gate type - controlled-v , ', 'control variable = 1,', e1[-2], 'target variable = 1,', e1[-1], ', Level-', ii, '\n')

        if len(d2) == 2:
            if d2[0] == 'v' and d2[1] == '+':
                e2 = alpha
                print('gate type - controlled-v+ , ', 'control variable = 1,', e2[-2], 'target variable = 1,', e2[-1], ', Level-', ii, '\n')

            if (d2[0] == 't' and d2[1] == '2') or (d2[0] == 'T' and d2[1] == '2'):
                e3 = alpha
                print('gate type - cnot gate , ', 'control variable = 1,', e3[-2], 'target variable = 1,', e3[-1], ' Level-', ii, '\n')
