# armstrong number
# 153 => 1^3 + 5^3 + 3^3 = 153 == armstrong number
# this program returns true if the given number is armstrong

n = int(input('enter a number '))
sum = 0

k = n 
while k > 0:
	sum += (k % 10) ** 3
	k //= 10

print(n, n == sum)
