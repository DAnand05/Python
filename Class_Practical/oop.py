class empl:
    __name=""
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile
        self.__name=name
    def display(self):
        print("Name = ",self.name,", Contact= ",self.mobile," spname=",self.__name)

obj=empl("Deep",9999999999)
obj.display()
print(obj.__name)