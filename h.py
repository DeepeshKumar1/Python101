
txt = open('deepesh.txt')
t = txt.readlines()
print t
c = {}

for i in t:
    if i.startswith('Deepssh'):
        c[i] = c.get(i, 0) + 1
        print c
        
       
        
