#total represents the first two rabbits
total=2
#n represents generation
n=1
#twice the growth rate to count 100
while total<=100:
        n=n+1
        total=2*total
        print(n,total)
