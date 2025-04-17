count = int(input(f"Enter Count Number :"))
number_list = list()

# Number and Count
number_most_count= 0
count_repeat = 0

for number in range(count):
    number_list.append(int(input(f"Enter Number {number+1} :")))

for number in range(len(number_list)):
    if(number_list.count(number_list[number])> count_repeat) :
        count_repeat = number_list.count(number_list[number])
        number_most_count = number_list[number]
    

print(f"Number List : {number_list}")
print(f"Count Repeat Number {number_most_count} : {count_repeat}")