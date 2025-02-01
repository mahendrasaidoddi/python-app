def square_numbers(nums):
    for i in nums:
        yield (i*i)     # so no return as we are returning generator

my_nums = square_numbers([1,2,3,4])
print(type(my_nums))  # print the type as class generator
print(next(my_nums))
print(next(my_nums))
print((my_nums)) # this wont work as this should be combination of both terators and decorators
