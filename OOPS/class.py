class Employee:
    employees = 0
    # def __init__(self, name) -> None:
    #     pass
    def __init__(self, name, id) -> None: # overrides the previous contructor
        self.name = name
        self.id = id
        Employee.employees+=1

    def display(self):
        print(f'{self.name} and id is {self.id}')


if __name__ == "__main__":

    emp1 = Employee('Dhanu', 1)
    # del emp.id
   
    emp1.display()

    emp2 = Employee('Kiran', 2)
    emp2.display()
    print(Employee.employees)

    print(emp1.__doc__)
    print(emp1.__dict__)
    print(emp1.__module__)    
    print(Employee.__name__)
    print(Employee.__bases__)