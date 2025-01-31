''' Custom Module:app.py'''  # Comment more than one line
import os,sys
# print("hi")

name="murthy" #global variale

def greet(ename):
    os.system('cls')
    data=[10,20,'Murthy'] # Private variable calling within the function '[]' means list
    print(type(data))
    print(data)

# Dict
    emp={'eno':101,'ename':'Laxmi'}
    print(type(emp))
    print(emp)

# To print the list of dictionary
    emps=[
        {'eno':101,'ename':'Laxmi'},
        {'eno':102,'ename':'Murthy'}
    ]
    print(type(emps))
    print(emps)

# To print the list of dictionary of the 2nd value
    emps=[
        {'eno':101,'ename':'Laxmi'},
        {'eno':102,'ename':'Murthy'}
    ]
    print(type(emps))
    print(emps[1])

# Tuple
    first,second=(100,200)
    print(first)

# Tuple
    first,second,third=(100,200,'mahendra')
    print(third)

if __name__=='__main__':  #This is an entry point for the function/application. From this file/name inside it we call multiple functions, modules integrates with dbs etc
    greet("kiran")
    sys.exit()
