
import random
kulki = {'a':2, 'b':2,'c':2,'d':2,'e':1,'f':2,'g':2,'h':2,'i':2,'j':2,'k':2,'l':2 }

gr1 = random.sample(kulki.items(),4)
print gr1
print gr1[0]
print gr1[0][1]+gr1[1][1]
print sum(j for i,j in gr1) 
