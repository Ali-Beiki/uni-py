with open("emp.dat", "w") as outfile:
    for i in range(3):
        print("Enter name, emno, salary :", end = "")
        name, empno, salary = input().split()
        record = name + "," + empno + ","  + salary + "\n"
        outfile.write(record)
with open("emp.dat", "r") as inf , open("high.dat", "w+") as outf:
    rec = inf.readline()
    while  len(rec) != 0:
          st = rec.split(",")
          newsalary = float(st[2]) + float(st[2]) * 10 / 100 
          newrec = st[0] + "," + st[1] + "," + str(newsalary) 
          outf.write(newrec + "\n")
          rec = inf.readline()
          #end of while
    outf.seek(0, 0)
    print("{0:10s} {1:10s} {2:10s}".format("Name", "EmpNo", "Salary"))
    print("-" * 30)
    rec = outf.readline()
    while  len(rec) != 0:
        rec = rec.strip("\n")
        st = rec.split(",")
        print("{0:<10s}{1:10s}{2:10s}".format(st[0], st[1], st[2]))
        rec = outf.readline() 
