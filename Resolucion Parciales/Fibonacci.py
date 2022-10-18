#Program to generate the Fibonacci Sequence till n
n=int(input("Enter the value of 'n': "))
#first two terms are first and second
first=0
second=1
sum=0
count=1
print("Fibonacci Sequence: ")
# Count should not be more then n.
while(count<=n):    
  print(sum)
  count+=1
  first=second
  second=sum
  sum=first+second	