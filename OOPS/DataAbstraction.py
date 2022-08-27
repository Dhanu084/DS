import random 
class Employee:
    __id = str(random.random())

    def __init__(self, name, salary) -> None:
        self.__salary = salary
        self.name = name
        self.__display()

    def __display(self):
        return self.name
    
if __name__=="__main__":
    e = Employee('dhanu', 1290900)
    print(e.name)
    # print(e.__display)
    # print(Employee.__id) -> returns error as __id is private
