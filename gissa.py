
import random 


slumptal = random.randint(1,10)
print (slumptal)
antalgissningar = 0
times = 1
vinst=False

while antalgissningar < 3 :
    antalgissningar = antalgissningar + 1
    spelarensval = input ("gissa ett tal ")
    

    if int(spelarensval) == slumptal:
        print("grattis du vann en anka ")
        vinst=True
        break


if vinst==False:
    print("\ntyvärr du vann  ingen anka denna gångn\n")
