def letterPath(M):
    if not M:
        return ''
    n = len(M)
    m = len(M[0])
    

    def F(G, s, p=[]):
        p = p + [s]
        if s not in G:
            return [p]
        P = []
        e = 0

        for n in G[s]:
            if n not in p:
                N = F(G, n, p)
                for n in N:
                    P.append(n)
            else:
                e += 1
        if e == len(G[s]):
            return [p]
        return P

    G = {}
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    
    #create graph of connected locations
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
    
