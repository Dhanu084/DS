class Calculation1:  
    def Summation(self,a,b):  
        return a+b;  
    
    def common1(self):
        print('Common from cal1')

class Calculation2:  
    def Multiplication(self,a,b):  
        return a*b;  

    def common(self):
        print('Common from cal2')
class Derived(Calculation2, Calculation1):  
    def Divide(self,a,b):  
        return a/b;  

d = Derived()  
# print(d.Summation(10,20))  
# print(d.Multiplication(10,20))  
# print(d.Divide(10,20))  
print(d.common1())

print(issubclass(Derived, Calculation1))
print(issubclass(Calculation1, Calculation2))

print(isinstance(d, Derived))