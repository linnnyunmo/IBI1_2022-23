#List the formula and calculate the total number of rabbits,loop through a range
#total represents the first two rabbits
#n represents generation
#twice the growth rate to count 100
#print the result
#The first two here inthe first generation
total=2
n=1
#Cycle over a total of less than 100
while total<=100:
        n=n+1
        total=2*total
        print(n,total)
# Get the results
