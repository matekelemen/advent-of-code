print((lambda s:sorted(s)[len(s)//2])((lambda S:[S(m) for m in ((lambda s:next(([] for c in l if (s.append(c) if 0<c else s.pop()==0 if s and c==-s[-1] else True)),s))([]) for l in (lambda m:((m[c] for c in l.strip()) for l in open("input").readlines() if l))({'(':1,'[':2,'{':3,'<':4,')':-1,']':-2,'}':-3,'>':-4})) if m])(lambda m:sum(v*5**i for i,v in enumerate(m)))))