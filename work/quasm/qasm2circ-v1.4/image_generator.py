import re

input_list = []
input_list1 = list
input_list2 = list
beta = list
tora = list
helium = list
delta = []
a3 = []
my_file = open('image.qasm', 'w')
my_file.close()


with open('converted_image.real', 'r+') as file:
    with open('image.qasm', 'a') as file_1:
        for line in file:
            input_list.append(line)
        a1 = input_list.index('.begin\n')
        input_list1 = input_list[0:a1]
        for i in range(len(input_list1)):
            a2 = str(input_list1[i])
            if 'input' in a2:
                a3 = re.split(' ', a2)
                a3 = a3[1:-1]
                for iii in range(len(a3)):
                    file_1.write('        qubit   {0}\n'.format(str(a3[iii])))
        a4 = input_list.index('.begin\n')
        input_list2 = input_list[a4+1:-1]
        file_1.write('\n\n')

with open('image.qasm', 'a') as lime:
    for i in range(len(input_list2)):
        alpha = input_list2[i]
        alpha = re.split('\\s', alpha)
        del alpha[-1]
        first_counter = a3[0]
        second_counter = a3[-1]
        if len(alpha) == 3:
            beta = alpha
            gamma = str(beta[0])
            if len(gamma) == 2:
                if gamma[0] == 'T' or 't' and gamma[1] == '2':
                    var1 = beta
                    lime.write('        ' + 'cnot' + '   ' + str(var1[-2]) + ',' + str(var1[-1]) + '\n')

                if gamma[0] == 'v' and gamma[1] == '+':
                    var2 = beta
                    lime.write('        ' + 'c-z' + '    ' + var2[-2] + ',' + var2[-1] + '\n')

            if len(gamma) == 1:
                if gamma[0] == 'v':
                    var3 = beta
                    lime.write('        ' + 'c-x' + '    ' + var3[-2] + ',' + var3[-1] + '\n')

        if len(alpha) == 2:
            helium = alpha[0]
            if len(helium) == 2:
                if helium[0] == 'v' and helium[1] == '+':
                    vrigo = alpha
                    lime.write('        ' + 'S' + '      ' + vrigo[-1] + '\n')

                if len(helium) == 2:
                    if helium[0] == 't' or 'T' and helium[1] == '1':
                        qwerty = alpha
                        lime.write('        ' + 'not' + '    ' + str(qwerty[-1]) + '\n')

            if len(helium) == 1:
                myvar = alpha
                lime.write('        ' + 'X' + '      ' + myvar[-1] + '\n')
