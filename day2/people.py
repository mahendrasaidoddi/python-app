import random # Builtin module
import time # Builtin module

# For testing the data, we need to have million records of data, i have used the below data and make them to have million records
names = ['Murthy', 'Kiran', 'Arun', 'Sita', 'Raj', 'Thomas'] 
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# Iterators
def people_list(num_people):
    result = [] #To mock created an empty result it will occupy the memony for storing the ressult
    for i in range(num_people): #Range is generator and below is the iterator code
        # Passing the data in dict
        person = {
                    'id': i, 
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

# Generator
def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person #Demand based fetching the data



#--------
# Test code
t1 = time.process_time()
people = people_list(100000) # We can change the 10000 value to anything to get as many record we want to 1000000, 224524546, 1425245253 etc
t2 = time.process_time()     
print("Time taken  with list iterator :{} secs".format(t2-t1)) # Format in time in c language format

# TO clean the memory accumulated by the data after processing which needs to be cleaned
import gc
del people # Even if the data is deleed, the data is still exists in heap memory
gc.collect()
t1 = time.process_time()
people = people_generator(10000)
t2 = time.process_time()
print("Time taken with Generator :{} secs ".format(t2-t1))


# This will result list the time of processing used by list iterator and generator.
#
