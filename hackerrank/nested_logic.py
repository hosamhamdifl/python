# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_date=list(map(int,input().strip().split()))
due_date=list(map(int,input().strip().split()))
fine=0
days_late=returned_date[0]-due_date[0]
months_late=returned_date[1]-due_date[1]
years_late=returned_date[2]-due_date[2]


if years_late>0:
    fine=10000
elif years_late<0:
    fine=0
elif months_late>0:
    fine=500*months_late
elif days_late > 0 and (returned_date[2] != due_date[2] + 1):
    fine=15*days_late
else:
    fine=0
print(fine)
