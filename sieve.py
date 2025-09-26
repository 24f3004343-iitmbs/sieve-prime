#prime number by Sieve of Eratosthenes using list removal
#works well for small/medium values of r
def  sieve(n):
    #generating prime numbers up to n using list removal method
    l=[i for i in range (2,n+1)]#list comprehension
    for i in range(2,(int(n**0.5))+1):
        j=0
        while j<len(l):
            if l[j]%i==0 and l[j]!=i:
                l.pop(j)# remove of multiples of i
            else:
                j=j+1            
    return l        
        
r=int(input('Enter range'))
prime=sieve(r)
print("Prime numbers are-"+str(prime))
