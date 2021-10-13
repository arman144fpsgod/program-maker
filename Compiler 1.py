import random
a = str(random.randint(1,10))
b = str(random.randint(1,10))
test = open("Testcompiler.txt", "w")
test.write(a)
test.write("\n")
test.write(b)
test.close()
