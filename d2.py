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

numbooks = []
libs_days = dict()
books_inlibs = dict()
for i in range(2,L*2+1,2) :
	lib = list(map(int,data[i].strip().split(" ")))
	sign = lib[0]
	id_lib = i//2 -1 
	#print(id_lib)
	
	libs_days[id_lib] = lib[1]
	
	books_inlib = data[i+1].strip().split(" ")
	books_inlibs[id_lib] = books_inlib
	
	if sign in numbooks :
		numbooks.sort(reverse=True)
		pos = numbooks.index(sign)
		libs = libs[:pos]+[id_lib]+libs[pos:]
	else :
		numbooks.append(sign)
		numbooks.sort(reverse=True)
		pos = numbooks.index(sign)
		libs = libs[:pos]+[id_lib]+libs[pos:]
num_books = []
#print(libs_days)
#print(libs)
cnt = 0
for lib in libs :
	#print(cnt)
	num = min(D - libs_days[lib] - cnt,len(books_inlibs[lib]) )
	if num < 1 : break
	num_books.append(min(D - libs_days[lib] - cnt,len(books_inlibs[lib]) ))
	cnt += 1


f_out = open("d2_out",'w')

f_out.write(str(len(num_books))+"\n")

for i in range(len(num_books)) :
	number = num_books[i]
	if number == 0 : continue
	f_out.write(str(libs[i]) +" "+str(num_books[i]) +"\n")
	f_out.write(" ".join(books_inlibs[libs[i]][:num_books[i]]) + "\n")

f_out.close()
