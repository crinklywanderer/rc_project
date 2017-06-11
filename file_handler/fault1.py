import re
global_list = []
sub_list = []
int_list = []
ip = []
ams = []
ams1 = []
fp = open('fault_tt.py', 'w')
fp.close()
with open('main1.txt') as file:
    for line in file:
        global_list.append(line)
    k = len(global_list)
    k -= 1
    if global_list[k] == "\n":
        del global_list[k]
    for ii in range(len(global_list)):
        int_list.append(global_list[ii])
        ini = re.split('\n', ''.join(int_list))
    k1 = len(ini)
    k2 = k1-1
    if ini[k2] == "":
        del ini[k2]
    print('final ini', ini)
    global_list = ini
    print(global_list)
    print('ENTER THE LEVEL YOU WANT TO INSERT (SINGLE) STUCK AT-0 OR STUCK AT-1')
    le_no = int(input(''))
    print('YOUR ENTERED LEVEL NUMBER :-', le_no)
    print('LEVEL DESCRIPTION GOES AS FOLLOWS')
    for iff in range(len(global_list[le_no])):
        ip.append(global_list[le_no])
        break
    ip_ = re.split(',', ''.join(ip))
    print('this is ip_', ip_)
    for m in range(len(ip_)):
        print(ip_[m])
    print('Enter Line Number where you want to insert fault')
    lio = int(input(''))
    k3 = len(ip)
    print('this is k3:', k3)
    if lio == k3:
        print('This is target line you can not insert fault here')
    print('Your desired line is :', ip_[lio])
    pp = str(ip_[lio])
    pp1 = pp + '=' + '0'
    print(pp1)

with open('tt_generator.py') as lo:
    for fi in lo:
        ams.append(fi)
    print(ams)





        



