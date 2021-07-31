f=open("bus.txt",'w')
for i in range(10):
	f.write("25 ")
f.close()

def bus():
	p=open("kmroute.txt",'w')
	for i in range(1,160,10):
		p.write(str(i))
		p.write(" ")
	p.close()
	
	print("Bus booking..")
	fr=int(input("From(District code):"))
	to=int(input("To(District code):"))
	
	p=open("kmroute.txt",'r')
	w=p.read().split()

	km=eval(w[fr])-eval(w[to])
	if(km<0):
		km=-km
	price=6+km
	
	choose=int(input("Enter bus number(1-10): "))
	print("Price= ",price)
	if(input("Do you prefer to take this ticket")=='n'):
		pass
	else:
		f=open("bus.txt")
		s=f.read().split()
		f.close()
		x=eval(s[choose+1])-1
		s[choose+1]=str(x)
		print(x)
		f=open("bus.txt",'w')
		for i in range(10):
			f.write(s[i])
			f.write(" ")
		f.close()		
					
		
while(True):
	bus()
	if(input("Do you want to try again")=='n'):
		break
