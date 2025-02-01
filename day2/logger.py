# Decorators
def logger(func):
    def wrapper(): # function name could be anything mahendra, navya, jessy, susmitha etc any but for best prctice we use wrapper
        print(f"Someone called {func.__name__}")
        func()
        print(f"{func.__name__} is successfully executed") # This way by pasiing before and after function this way we can track what the activity is done
    return wrapper






@logger #used the decorator logger above the def function, this will 1st initially executes the logger function and then go with proceedData function
# This is attribute programming in 
def proceedData():  #
    print("connecting to DB")
    print("data processed")

# To invoke this
proceedData()