from functools import reduce
def determinantOne(n):
    M = 10**9+7
    c = [20,32,64]
    o = 0
    l = 64
    a = 0
    s = sum(c)
    
    #find all primes between 3 and n
    if n <= 3:
        return sum(c[:n])
    m = n + 1
    S = [True] * m
    for i in range(3,int(m**0.5)+1,2):
        if S[i]:
            S[i*i::2*i]=[False]*((m-i*i-1)//(2*i)+1)
    P = {i:1 for i in range(3,m,2) if S[i]}
    
    
    #if you solve the first 105 or so with a brute force solution - a pattern can be discerned (or look on OEIS for the first 39 or so)
    #Let c = [] be a list of all differences between adjacent values of determinantOne (one-based) for values from 1 to n
    #If the prime factorization of n is:
    #A^a*B^b
    #The value of c[n] will be equal to:
    #c[n] = (c[A]*A**(a-1) * c[B]*B**(b-1))/(32**(a+b-1))

    #This does not work when n is prime - in this case:
    #let m be the last prime number before n
    #c[n] = c[m] + 64*(n-m)/2
    
    #After all this, just add together all values in c[1:n] inclusive to find
    #the total number of 2x2 matrices which satisfy the criteria.

    
    #function to find prime factors
    def F(n):
        i = 2
        b = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                b.append(i)
        if n > 1:
            b.append(n)
        return b

    for i in range(4,n+1):
        if not i%2: #if i is even
            j = i//2
            if not (j)%2: #if i/2 is even
                a = c[j-1]*2
            else:
                a = c[j-1]
            s = s%M + a%M
        else: #if i is odd
            if i in P:
                a = (1+o)*64+l
                s += a
                l = a #reset the most recent prime to l
                o = 0
            else:
                o += 1
                f = F(i)
                g = set(f)
                a = 1
                for v in g:
                    r = f.count(v)-1
                    a *= c[v-1]*(v**r)
                    d = 32**(len(g)-1)
                s = s%M + (a//d)%M
                a = a//d
        c.append(a)
                
    return s