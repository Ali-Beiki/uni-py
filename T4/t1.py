count_std =3

std_name_list =list()
std_gpa_list =list()
std_code_list =list()

#set data
for std in range(count_std):
    std_name = str(input(f"Enter Student Name {std+1} :"))
    std_gpa = int(input(f"Enter Student GPA {std+1} :"))
    std_code = str(input(f"Enter Student Code {std+1} :"))

    std_name_list.append(std_name)
    std_gpa_list.append(std_gpa)
    std_code_list.append(std_code)


#find larg
max_gpa = max(std_gpa_list)
std_max_index = std_gpa_list.index(max_gpa)

#find min
min_gpa = min(std_gpa_list)
std_min_index = std_gpa_list.index(min_gpa)

print(f"-> Max GPA :{max_gpa}, Student Code :{std_code_list[std_max_index]} Student Name :{std_name_list[std_max_index]} ")
print(f"-> Min GPA :{min_gpa}, Student Code :{std_code_list[std_min_index]} Student Name :{std_name_list[std_min_index]} ")

#show
print("Main List")
print(std_name_list)
print(std_gpa_list)
print(std_code_list)

# remove by student code

#get code
std_remove_code = str(input(f"Enter Student Code :"))
# remove
if std_remove_code in std_code_list :
    #get index
    std_remove_code_index = std_code_list.index(std_remove_code)


    print(f"delete {std_name_list[std_remove_code_index]} success !")

    # remove
    std_code_list.remove(std_remove_code) # delete in list by item
    del std_name_list[std_remove_code_index] # delete in list by index
    del std_gpa_list[std_remove_code_index]

#show
print("Main List")
print(std_name_list)
print(std_gpa_list)
print(std_code_list)

# for log
std_list = []

# create copy for save index 
for i in range(len(std_name_list)):
    std_list.append({
        "name": std_name_list[i],
        "gpa": std_gpa_list[i],
        "code": std_code_list[i]
    })

# sort by character
std_list.sort(key=lambda student: student["name"])

# end result
print("Sorted List:")
for student in std_list:
    print(f"Name: {student['name']}, GPA: {student['gpa']}, Code: {student['code']}")
