# Prints Prime Numbers from 2 to 100
# loops can have "else" block, this will execute when innner for or while conditions fails

for i in range(2, 101):
	for j in range(2, i):
		if i % j == 0:
			print(i, "is not a prime number")
			break
	else:                                 # this is exectuted when the above for loop condition fails
		print(i, "is a prime number")     # (If the above "if" condition executes, then "else" part is not executed)
