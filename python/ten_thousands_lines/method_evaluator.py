import time
import que_method_1 
import recursive_method_1

# set up
string_length = 4

#Runnind Tests
start_time = time.time()
que_method_1.generate_combinations(string_length)
end_time = time.time()
execution_time = end_time - start_time

print( f" que_method_1.generate_combinations took {execution_time} seconds to execute ")


start_time = time.time()
recursive_method_1.generate_combinations("",string_length)  # magic empty string needed for internal conversion
end_time = time.time()
execution_time = end_time - start_time

print( f" recursive_method_1.generate_combinations took {execution_time} seconds to execute ")

