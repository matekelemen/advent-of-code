(lambda E:[[E(i,j,open(f"day_{i}/part_{j}.py").read().replace("input",f"day_{i}/input").strip()[6:-1],open(f"day_{i}/readme.md").read()) for j in (1,2)] for i in range(1,26)])(lambda i,j,C,R:(print(f'day {i}/{j}: ',end=''),exec(f"\ntry:\n print('OK') if eval(C)=={(lambda s,i:int(s[i:i+s[i:].find('</code>')]) if s[i:i+s[i:].find('</code>')].isdigit() else None)(*(lambda s,k:(s,s.find(k)+len(k) if j==1 else s.rfind(k)+len(k)))(R,'Your puzzle answer was <code>'))} else print('INCORRECT')\nexcept Exception as e:print('ERROR')",{'C':C}) if C and R else print("INCOMPLETE")))