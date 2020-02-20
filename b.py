from sys import argv

def to_int(n) :
	return int(n)

fil = open(argv[1],'r')
data = fil.read().strip().split("\n")
#print(data)
#print(data[0])
B,L,D = list(map(int,data[0].split(" ")))

books = data[1]
#print(B,L,D)
libs = []

numdays = []
libs_days = dict()
books_inlibs = dict()
for i in range(2,L*2+1,2) :
	lib = list(map(int,data[i].strip().split(" ")))
	sign = lib[1]
	id_lib = i//2 -1 
	
	libs_days[id_lib] = lib[1]
	
	books_inlib = data[i+1].strip().split(" ")
	books_inlibs[id_lib] = books_inlib
	
	if sign in numdays :
		pos = numdays.index(sign)
		libs = libs[:pos]+[id_lib]+libs[pos:]
	else :
		numdays.append(sign)
		numdays.sort()
		pos = numdays.index(sign)
		libs = libs[:pos]+[id_lib]+libs[pos:]
num_books = []
#print(libs_days)
#print(libs)
cnt = 0
for lib in libs :
	num_books.append(D - libs_days[lib] - cnt)
	cnt += 1


f_out = open("b_out",'w')

f_out.write(str(len(libs))+"\n")

for i in range(len(libs)) :
	f_out.write(str(libs[i]) +" "+str(num_books[i]) +"\n")
	f_out.write(" ".join(books_inlibs[libs[i]][:num_books[i]]) + "\n")

f_out.close()
