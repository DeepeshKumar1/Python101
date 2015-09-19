a = raw_input("Enter the filename")
txt = open(a)
for i in txt:
    print i.readlines()
    
