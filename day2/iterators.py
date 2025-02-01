# Iterators design pattern
data=[10,20,30,40]
print(data[2]) # 
for i in data:
    print(i) # This is iterator

data=[10,20,30,40]
d = iter(data) # This is iterator
print(type(d))
print(d.__next__()) #d is iterator and Used special function call __next__ give the pagination 1st value
print(next(d))  # This will print the next value after executing above line
print(next(d))
print(next(d))
print(next(d)) # Once the data is out of the scope an the iterations are close, it will throw an stop iteration callback.
