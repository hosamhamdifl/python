# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
od = OrderedDict()
input_data = ''
input_list = []
for i in range(n):

    input_data = input()
    input_list = input_data.rsplit(' ',1)
    input_list[1] = int(input_list[1])
    if input_list[0] not in od.keys():
        od[input_list[0]] = input_list[1]
    elif input_list[0] in od.keys():
        od[input_list[0]] += input_list[1]


for i,key in enumerate(od):
    value=od[key]
    print(f"{key} {value}")
