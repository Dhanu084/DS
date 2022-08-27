class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks
        
    def average(self):
        return sum(self.marks)/len(self.marks)
    

class WorkingStudent(Student):
    def __init__(self, name, marks, salary) -> None:
        super().__init__(name, marks)
        self.salary = salary

    @staticmethod
    def getStudent():
        print('hola')

    def getStudentInfo(self):
        pass
    
    def __repr__(self) -> str:
        return f'{self.name} with marks {self.average()} gets {self.salary}$'


workingStudent = WorkingStudent('Rolf',[8,7.5,9.2,8.2],15.50)
print(workingStudent)
workingStudent.getStudent()