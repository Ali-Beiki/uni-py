count =int(input("Enter count loop :"))

def fibonacci(old,new,count):
   for _ in range(count) :
      print(old)
      old,new = new ,old +new

fibonacci(1,1,count)