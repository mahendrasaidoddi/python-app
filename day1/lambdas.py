def check(x):
    ''' check fn will '''

def add5(val):  #add5 is the name of the function

    return val+5

print(add5(100))

#single line functions are called lambda functions
add6=lambda val:val+5

print(type(add6)) #print type of function
print(add6(300))

sm=lambda x:True if x.startswith('M') else False

print(sm('mahendra')) # Pyhton is case sensitive if the value in 'mahendra' it will respond as false
print(sm('Mahendra'))


# map
alist=['learn','python','step','by','step']
output=map(lambda x:x.upper(),alist) # if you try to print the map object as it is procssing you cant get the output
print(type(output))
print(output)

alist=['learn','python','step','by','step']
output=list(map(lambda x:x.upper(),alist)) #to print the value of the map object need to use the lsit type
print(type(output))
print(output)


#using def
def converter(mylist):
    result=[]
    for item in mylist:
        citem=item.upper()
        result.append(citem)
        print(citem)
        return result
    
# Filter
scores = [66,54,76,87,85,74,81,65]
def is_A_student(score): #used  def function
    return score > 75 

over_75 = list(filter(is_A_student,scores))
print(over_75)


scores = [66,54,76,87,85,74,81,65]
over60 = list(filter(lambda x:x>60,scores)) #used lambda function in the same 
print(over60)


scores = [66,54,76,87,85,74,81,65]
checker=lambda x:x>50  #used checker variable here and called in below
over60 = list(filter(checker,scores))
print(over60)

#sort
list1=[('eggs',5.25),('honey',7.58),('carrots',1.4)]
list1.sort(key= lambda x:x[1],reverse=1) #True=1, False=2 in the reverse order
print(list1)

list1=[('eggs',5.25),('honey',7.58),('carrots',1.4)]
list1.sort(key= lambda x:x[1],reverse=0) #True=1, False=2 in the reverse order
print(list1)

list1=[('eggs',5.25),('honey',7.58),('carrots',1.4)]
list1.sort(key= lambda x:x[1]) #default order
print(list1)

list1=[('eggs',5.25),('honey',7.58),('carrots',1.4)]  
list1.sort(key= lambda x:x[0]) #True=1, False=2 in the reverse order
print(list1)  #x:x[0] soreted by 1st characters

import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
squarer = lambda t:t**2
squares = np.array([squarer(xi) for xi in x])
print(type(squarer))
print(type(squares))
print(squares)