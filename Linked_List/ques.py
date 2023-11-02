'''
Create a Class of an Employee with attributes 
empid,name,salary and also define method to access properties of employee.
'''

class employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setempid(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsalary(self,salry):
        self.salary=salry
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
e1=employee(101,'popat',20000)
e2=employee()
e2.setempid(102)
e2.setname('Alice')
e2.setsalary(30000)

print(e1.getempid(),e1.getname(),e1.getsalary())
print(e2.getempid(),e2.getname(),e2.getsalary())