import time


def calculate_time(func):
    def wrapper(n):
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        excuation_time = end_time - start_time
        print(f"the execution time is {excuation_time}")
        return result
    return wrapper
    

@calculate_time
def create_list(n):
    my_list = []
    for i in range(1,n+1):
        my_list.append(i)
    return my_list
        
    
    
    
    
    
user_input = int(input())
result = create_list(user_input)
print(result)
