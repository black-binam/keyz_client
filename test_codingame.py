"""
def sequ(num):
    try:
        assert num<10000, 'Erreur'
        s = str(num)
        lst = list(s)
        seq = int(num)
        for n in s:
            seq+=int(n)
        return seq

    except AssertionError :
        return'error'

    

def test(s1,s2):
    joint =None
    
   
    v1 = [sequ(s1)]
    v2 = [sequ(s2)]

    for n in range(0,10):
        if n in v2:
            joint = n
            return joint 
        else:
            v1.append(sequ)

    return joint




print(test(471, 480))


v1 =[sequ(471)]
v2 = [sequ(480)]

for n in range(0,10):
    v1.append(sequ(v1[n]))
    v2.append(sequ(v2[n]))



print(v1,v2, sep='\n')
for i in v1:
    if i in v2:
        print(i)
        break
"""

def solve(width, height, length, mass):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    lst = [width,height, length, mass]
    
    w = width
    h = height
    l = length
    m = mass

    vol = w*h*l

    lourd = False
    enc = False
   

    #---------------------------------
    if m>=20:
        lourd = True

    if w>=150 or h>=150 or l>=150 or vol>= 1000000:
        
        #print(w or h or l >=150)

        enc =True
    #---------------------------------



    if lourd==False and enc == False:
        
        return "STANDARD"
    
    
    elif lourd == True or enc == True:
        print('lour, enc ',lourd, enc)
        if lourd == True and enc == True:

            return 'REJECTED'
        else:

            return "SPECIAL"
   
    
    elif lourd==True and enc == True:

        return "REJECTED"
    


    return "aucune reponse"





print(solve(120,100,110,30))