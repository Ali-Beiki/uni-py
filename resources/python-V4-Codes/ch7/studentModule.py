class student:
    def __init__(self, stName, stEmail, stAve):
        self.name = stName
        self.email = stEmail
        self.ave = stAve
    def display(self):
        print(self.name, self.email, self.ave)
    def sendemail(self):
        print("We are going to send mail")
    def verify(self):
        print("We are going to verify the mail")
