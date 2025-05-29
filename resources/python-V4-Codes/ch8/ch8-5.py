class file:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print("init method called")
    def __enter__(self):
        print("enter method called")
        self.open_file = open(self.filename, self.mode)
        return self.open_file
    def __exit__(self, *args):
        print("exit method called")
        self.open_file.close()
#-----------------------------------
with file("test.dat", "w") as infile:
    print("with statement block")
    infile.write("This is a test")
    
