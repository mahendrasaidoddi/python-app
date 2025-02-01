# Oops module
# Class name should start with capital letter so that it will be identified object
class Employee(object):
    #constructor 
    def __init__(self,empno,ename,salary): # We can also pass default values like salary=500 #Parameters like empno,ename,salary is not accepted in class so re iterating them to below data to we can call them
        self.eno=empno  #These are called instance variables / properties
        self.name=ename
        self.pay=salary
    
    def showDetails(self): # Instance  method
        print("Emp No ", self.eno)
        print("Emp Name ", self.name)
        print("Salary ", self.pay)



if __name__=='__main__':
    e1=Employee(101,'Murthy',50000)
    e1.showDetails()
    e2=Employee(102,'Mahendra',850000)
    e2.showDetails()


