def donkeyKongCountry(s):
    N = []
    n = ''
    b = 'Int32[]'
    for l in s:
        g = re.match('^([A-Z0-9]+) = ([A-Za-z- ]+)',l)
        N += ['0x'+g.group(1)]
      
        n = g.group(2).lower().split(' ')
        n = n[-1] if n[-1] else n[-2]

    n = re.sub('-','_',n)
    #print name
    return b+' '+n+'=new '+b+' {'+','.join(N)+'}'