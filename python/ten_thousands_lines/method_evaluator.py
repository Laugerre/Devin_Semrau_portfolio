import time
import dummy_que_method 
import dummy_recursive_method

# set up
string_length = 4

#Runnind Tests
start_time = time.time()
dummy_que_method.generate_combinations(string_length)
end_time = time.time()
execution_time = end_time - start_time

print( f" dummy_que_method.generate_combinations took {execution_time} seconds to execute ")


start_time = time.time()
dummy_recursive_method.generate_combinations("",string_length)  # magic empty string needed for internal conversion
end_time = time.time()
execution_time = end_time - start_time

print( f" dummy_recursive_method.generate_combinations took {execution_time} seconds to execute ")
