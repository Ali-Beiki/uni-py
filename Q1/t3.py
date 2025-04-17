column_count =3
row_count =5
list_number =[]

# set data
for col in range(column_count):
    row =[]
    for r in range(row_count):
        num = int(input(f"Enter [{col}][{r}]"))
        row.append(num)
    list_number.append(row)

# transposed

# start in .... 

print(list_number)