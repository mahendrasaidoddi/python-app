# PROFILING PYTHON FUNCTION

import time

def profiler(func):
    """Print the runtime of the decorated function"""
    def wrapper_timer(*args,**kwargs):
        start_time = time.perf_counter()
        value=func(*args,**kwargs)
        end_time = time.perf_counter()
        run_time= end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs") #f - string, {run_time:.4f} :.4f removes the last four decimals, if we keey .2f then it will remove last 2 decimals
        return value
    return wrapper_timer



@profiler
def algorithm(num_times):
    for _ in range(num_times):  # _ is a thow away variable - dummy variable
        sum([i**2 for i in range(10000)]) # this [i**2 for i in range(10000)] is list comprehension replacement of lambda

#test code
algorithm(1)
algorithm(100)
algorithm(999)