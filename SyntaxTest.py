total = 0

def sum(arg1, arg2) :
    total = 1
    print(total)
    return total

sum(10,20)
print(total)

class Employee:
    'This is math tool class!'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        Employee.empCount -= 1

    def displayEmpCount():
        print ('count: ', Employee.empCount)

    def displayEmpCount():
        print ('count: ', Employee.empCount)

emp1 = Employee("JH", 7000)

emp2 = Employee("JE", 9000)

del emp2

Employee.displayEmpCount()

