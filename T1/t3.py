hour =int(input("Enter a Hour Number (H) :"))
minutes =int(input("Enter a Minutes Number (M) :"))
seconds =int(input("Enter a Seconds Number (S) :"))

total =(hour *60*60)+(minutes*60)+ seconds

print("hour (h) : {0:5d} ,minutes (m) : {1:2d} ,seconds (s) : {2:2d} ,Total Seconds (s) :{3:2d}".format(hour,minutes,seconds,total))
