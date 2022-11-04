print([(a,b,c) for a in range (1,100) 
                for b in range(1,100) 
                for c in range(1,100) 
                if c*c == b*b + a*a])