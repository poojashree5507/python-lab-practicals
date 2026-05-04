#in module file
def factors(n):
    factors = []
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
    return factors
def primefactors(n):
    prime= []
    i=2
    while i<=n:
        if n % i == 0:
            prime.append(i)
            n=n/i
        else:
            i+=1
    return prime
#in main
import fn_module
n=int(input("Enter a number: "))
print("factors are:")
print( fn_module.factors(n))
print("Primefactors are:")
print(fn_module.primefactors(n))
