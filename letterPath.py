def letterPath(M):
    if not M: #if the provided map is empty, return ''
        return ''
    #find the size of the provided letter map
    n = len(M)
    m = len(M[0])
    
    #recursive path finding algorithm a la https://www.python.org/doc/essays/graphs/
    def F(G, s, p=[]):
        p = p + [s] #add current location to path
        if s not in G: #if there is nowhere to go from current location, return path
            return [p]
        P = [] #initialize list of all possible paths
        e = 0 #initialize a variable to keep track of the length of the current path

        for n in G[s]: #iterate over all "directions" you can go from current letter
            if n not in p: #but only if the letter is not already in the path
                N = F(G, n, p)
                for n in N:
                    P.append(n)
            else:
                e += 1
        if e == len(G[s]): #if the path uses all letters, return it as there is no way to make a longer path
            return [p]
        return P

    G = {}
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    
    #create graph of connected locations - iterate over the full map and find all letter connected
    #orthogonally to the current location, add to a dictionary (G) that contains the mapped paths
    for i in range(n):
        for j in range(m):
            for k in range(4):
                dy,dx = d[k]
                if 0 <= i + dy <= n-1 and 0 <= j + dx <= m-1:
                    if M[i][j] != M[i+dy][j+dx]:
                        if (i,j) in G:
                            G[(i,j)] += [(i+dy,j+dx)]
                        else:
                            G[(i,j)] = [(i+dy,j+dx)]
    h = ''
    #call function to find all paths from each starting point
    for i in range(n):
        for j in range(m):
            s = (i,j)
            for p in F(G, s):
                s = ''.join([M[y][x] for y,x in p])
                if len(s) >= len(h):
                    if s > h:
                        h = s
    return h

    ##Example driver:
    #M = [[a,b,c],[d,e,f],[g,h,i]]
    #answer = letterPath(M)
    ##answer should be "ihgdefcba" - see letterPathREADME.md
    
