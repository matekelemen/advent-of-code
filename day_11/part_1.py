print((lambda l:sum([[l.__setitem__(i,1 if v==-1 else v+1) for i,v in enumerate(l)],(lambda l,s:sum(bool([l.__setitem__(i,-1),[[l.__setitem__(n,l[n]+1) if 0<=l[n] else 0,s.append(n) if 9<l[n] and not(n in s) else 0] for n in (j for j in [i-10,i+10]+([i-11,i-1,i+9] if i%10 else [])+([i-9,i+1,i+11] if (i+1)%10 else [])  if 0<=j and j<100)]]) for i in s))(l,[i for i,v in enumerate(l) if 9<v])][1] for _ in range(100)))([int(c) for c  in open("input").read() if c and c!='\n']))