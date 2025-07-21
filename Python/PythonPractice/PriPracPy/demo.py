print("Check Even or Odd")

num=int(input("enter the number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")
'''------------------------------------------------------'''

print("Find the largest of 3 numbers")
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a, "is largest")
elif b>=c and b>=a:
    print(b, "is largest")
else:
    print(c, "is largest")
'''----------------------------------------------------------'''

print("Factorial")
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial of ",n,"is", fact)
'''---------------------------------------------------------'''

print("Prime numbers")

p=int(input("enter the number: "))
is_prime=True

if p<=1:
    is_prime=False
else:
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            is_prime=False
            break
if is_prime:
    print(p, "is a prime  number")
else:
    print(p, "is not a prime number")
'''--------------------------------------------'''

print("FROM 1 to 100 PRIME NUMBERS")

for number in range(1,101):
    if num<=1:
        continue
    is_primes=True

    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            is_primes=False
            break
    if is_primes:
        print(number, end= " ")