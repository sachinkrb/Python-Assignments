def countdown(n):
    if n >= 0:
        print('Blastoff!')
        
    else:
        print(n)
        countdown(1+n)
    
countdown(-3)
