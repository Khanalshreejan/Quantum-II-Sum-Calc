# This is initializing two different sums
sum_of_integers = 0
sum_of_squares = 0

# Given n
n = 100000000  #I am using smaller number here i.e 100 millions since performing this code 
#for something in the order of 10^27 is not feasible in my computer.

# Loop from 1 to n
for k in range(1, int(n) + 1): #when using range () we need to add +1 for the last number
    sum_of_integers += k
    sum_of_squares += k**2

# Print Output of the sums
print(f"Sum of the first {n} integers: {sum_of_integers}")
print(f"Sum of the squares of the first {n} integers: {sum_of_squares}")

#Output: Sum of the first 100000000 integers: 5000000050000000
         #Sum of the squares of the first 100000000 integers: 333333338333333350000000

#Hence clearly two approaches do not give approximately same order of numbers. We can see this from the output above.
