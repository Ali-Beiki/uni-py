import numpy as nm

countStudent = int(input(f"Enter Count Student :"))
students =list()

for student in range(countStudent):
    students.append(int(input(f"Enter Score Student {student+1} :")))

print(f"List Score :{students}")
print(f"Average Score :{nm.average(students)}")

indexLargest =nm.where(students > nm.average(students) )
print(indexLargest)
print(f"Score Largrst Average :{len(indexLargest[0])}") //❌

