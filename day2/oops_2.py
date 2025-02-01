# Oops module
# Class name should start with capital letter so that it will be identified object
class Employee(object):
    #constructor 
    def __init__(self,empno,ename,salary): # We can also pass default values like salary=500 #Parameters like empno,ename,salary is not accepted in class so re iterating them to below data to we can call them
        self.eno=empno  #These are called instance variables / properties
        self.name=ename
        self.pay=salary
        self.bonus=10000 # THIS WAY WE CAN add the bonus to the employees but 
        self.__bonus1=20000  # __bonus "__" This will make as private instance property
    
    def showDetails(self): # Instance  method
        print("Emp No ", self.eno)
        print("Emp Name ", self.name)
        print("Salary ", self.pay)
        print("total amt",self.pay+self.bonus)
        print("total amt",self.pay+self.__bonus1)     




if __name__=='__main__':
    e1=Employee(101,'Murthy',50000)
    e1.showDetails()
    e2=Employee(102,'Mahendra',850000)
    e2.showDetails()
    e1.bonus=50000 # As we pass the value, this will encapsulate the data which means there is no data privacy and security
    print(e1.bonus)
    e1.showDetails()
    print(e1.__bonus1) #It will throw an error when you call the attributes outside the class