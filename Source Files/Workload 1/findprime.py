import datetime, sys, math

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

# Function to print message
def print_prime(x):
  print " Prime : %7i " %x
 
# Function to search for prime numbers
# within number range
def find_primes(upper_limit):
	count=0
	for num in range(lower, upper+1):
		if num > 1:
			for i in range (2,num):
				if (num % i) == 0:
					break
			else:
				print(num)  
				count = count+1
	return count

# Check if the script was called with a
# parameter. Use that as the upper limit
# of numbers to search
if len(sys.argv) != 2:
  upper_limit=1000000
else:
  upper_limit=int(sys.argv[1])

# Record the current time
startTime = datetime.datetime.now()
 
# Start the process
print ""
print "Starting ..."
print ""
count = find_primes(upper_limit)
print ""
 
# Measure and print the elapsed time
elapsed=datetime.datetime.now()-startTime
print " Found %d primes in %s" %(count,elapsed)
print ""
