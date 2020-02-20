from sys import argv

fil = open(argv[1],'r')
data = fil.read().strip().split("\n")
print(data)
print(data[0])
B,L,D = tuple(data[0].split(" "))

print(B,L,D)

