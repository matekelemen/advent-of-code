print((lambda a:sum(1+v for i,v in enumerate(a) if all(v<a[k] for k in [i-100,i+100]+([i-1] if i%100 else [])+([i+1] if (i+1)%100 else []) if 0<=k and k<len(a))))([int(c) for c in open("input").read() if c and c!='\n']))