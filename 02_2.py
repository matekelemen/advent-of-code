print((lambda c: c.real*c.imag)((lambda l: sum(v.real*v.imag+v.imag*1j for v in l))((lambda l: [sum(v[1] for v in l[:I] if v[0]=='d')-sum(v[1] for v in l[:I] if v[0]=='u')+V[1]*1j for I,V in enumerate(l) if V[0]=='f']) ([[l[0],int(l.strip()[l.rfind(' ')+1:])] for l in open("input").readlines()]))))
