# Custom Iterator
class Head:
    def __init__(self,size=5): #adding the default value of size
        self.num=1 #Taking num property as size

    def __iter__(self): # Override the iter class to iterator class
        return self
    
    def __next__(self):
        # Write DB, REST API calls or load local csv files data
        if self.num<=5:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration # Here are using try and exception approach when the iteration completes
        
# --------------
# test code
values=Head(100)
'''
print(values.__next__()) # this will go each iteration and print value 1
print(values.__next__()) # this will go each iteration and print value 2
print(values.__next__()) # this will go each iteration and print value 3
print(values.__next__()) # this will go each iteration and print value 4
print(values.__next__()) # this will go each iteration and print value 5
print(values.__next__()) # this will go each iteration  it will throw StopIteration '''
for i in values:  # Another approach used by for iteration, because of this def __iter__(self) class it will stop after 5 iterators
    print(i) 