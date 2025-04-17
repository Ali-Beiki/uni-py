# تعریف توابع اول
def find_gpa_max():
    max_gpa = max(std_gpa_list)
    i = std_gpa_list.index(max_gpa)
    print(f"-> Max GPA :{max_gpa}, Student Code :{std_code_list[i]} Student Name :{std_name_list[i]}")

def find_gpa_min():
    min_gpa = min(std_gpa_list)
    i = std_gpa_list.index(min_gpa)
    print(f"-> Min GPA :{min_gpa}, Student Code :{std_code_list[i]} Student Name :{std_name_list[i]}")

def show():
    print("Main List")
    print(std_name_list)
    print(std_gpa_list)
    print(std_code_list)

def remove_student():
    code = input("Enter Student Code: ")
    if code in std_code_list:
        i = std_code_list.index(code)
        print(f"Deleted {std_name_list[i]} successfully!")
        std_code_list.pop(i)
        std_name_list.pop(i)
        std_gpa_list.pop(i)
    else:
        print("Student code not found.")

def sort_by_name():
    global std_name_list, std_gpa_list, std_code_list  # اضافه‌شده

    std_list = []
    for i in range(len(std_name_list)):
        std_list.append({"name": std_name_list[i], "gpa": std_gpa_list[i], "code": std_code_list[i]})
    std_list.sort(key=lambda s: s["name"])
    print("Sorted List:")

    std_name_list_copy = []
    std_gpa_list_copy = []
    std_code_list_copy = []

    for s in std_list:
        print(f"Name: {s['name']}, GPA: {s['gpa']}, Code: {s['code']}")
        std_name_list_copy.append(s['name'])
        std_gpa_list_copy.append(s['gpa'])
        std_code_list_copy.append(s['code'])

    std_name_list = std_name_list_copy
    std_gpa_list = std_gpa_list_copy
    std_code_list = std_code_list_copy


# بعد تعریف توابع، حالا بریم سراغ دریافت داده‌ها و منو
count_std = int(input("Enter Count Student: "))
std_name_list = []
std_gpa_list = []
std_code_list = []



for i in range(count_std):
    name = input(f"Enter Student Name {i+1}: ")
    gpa = int(input(f"Enter Student GPA {i+1}: "))
    code = input(f"Enter Student Code {i+1}: ")
    std_name_list.append(name)
    std_gpa_list.append(gpa)
    std_code_list.append(code)

show()
find_gpa_min()
find_gpa_max()
remove_student()
show()
sort_by_name()
show()
