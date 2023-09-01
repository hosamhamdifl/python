from collections import namedtuple

n = int(input())
col_names = input().split()
col_names = ['class_' if x.lower() == 'class' else x for x in col_names]
Student = namedtuple('Student', col_names)
students = []
for _ in range(n):
    fields = input().split()
    student = Student(*fields)
    students.append(student)

# Now you can access the fields of each student like this:
avg=0
sum=0
c=len(students)
for student in students:
    sum+=float(student.MARKS)
avg=sum/c
print(avg)