class student:
              def __init__(self,name,age,city):
                            self.name=name
                            self.age=age
                            self.city=city
              def details(self):
                            print(self.name,"age is",self.age,"and she is from",self.city)
                            
              @staticmethod
              def prints():
                            print("welcome to our team")
o=student("vaishnavi",20,"pudukkottai")
o.details()
o.prints()


