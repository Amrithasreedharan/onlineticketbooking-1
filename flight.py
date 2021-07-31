f=open("flight.txt",'w')
for i in range(10):
        f.write("25 ")
f.close()

def flight():
        p=open("distance.txt",'w')
        for i in range(1,16000,10000):
                p.write(str(i))
                p.write(" ")
        p.close()

        print("flight booking..")
        fr=int(input("From District ):"))
        to=int(input("To District ):"))

        p=open("kmroute.txt",'r')
        w=p.read().split()

	p.close()

        print("flight booking..")
        fr=int(input("From District ):"))
        to=int(input("To District ):"))

        p=open("distance.txt.txt",'r')
        w=p.read().split()

        km=eval(w[fr])-eval(w[to])
        if(km<0):
                km=-km
        price=1500+km

        choose=int(input("Enter flight number(1456-3456): "))
        print("Price= ",price)
        if(input("Do you prefer to take this ticket")=='n'):
                pass
        else:
		if(km<0):
                km=-km
        price=1500+km

        choose=int(input("Enter flight number(1456-3456): "))
        print("Price= ",price)
        if(input("Do you prefer to take this ticket")=='n'):
                pass
        else:
                f=open("flight.txt")
                s=f.read().split()
                f.close()
                x=eval(s[choose+1])-1
                s[choose+1]=str(x)
                print(x)
                f=open("flight.txt",'w')
                for i in range(10):
                        f.write(s[i])
                        f.write(" ")
		 f.close()


while(True):
        bus()
        if(input("Do you want to try again")=='n'):
                break

