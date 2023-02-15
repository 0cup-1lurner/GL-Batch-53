"""
	Before the try block change the divisor to a non-zero integer check which block
	of executes(except or else or both).

	Repeat the same process by changing the divisor to zero.

"""
divisor = 0  # Change the divisor here
try:
    result = 12/divisor  
except ZeroDivisionError:
    print("Please use a non-zero num as a divisor")
else:
    # If there is no exception this block is executed
    print("Block 3")

print("2nd line")
