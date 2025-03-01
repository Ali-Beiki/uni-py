count =int(input("Enter count loop :"))

def fibonacci(old,new,count):
   if count != 0 :
      print(old)
      old,new =new,old+new
      fibonacci(old,new,count-1)
    
fibonacci(1,1,count)