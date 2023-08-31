s= input()
lower_s=''
upper_s=''
int_s_odd=''
int_s_even=''
for i in s:
    if i.isnumeric():
        if int(i)%2==0:
            int_s_even+=i
        else:
            int_s_odd+=i
    elif i.islower():
        lower_s+=i
    elif i.isupper():
        upper_s+=i

print(''.join(sorted(lower_s)+sorted(upper_s)+sorted(int_s_odd)+sorted(int_s_even)))

