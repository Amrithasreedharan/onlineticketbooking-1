def movie ():
    file1=open ("mov.txt",'r')
    file2=open ("bill.txt",'a')
    print(file1.read())
    m=input ("choose the movie you need :")
    d=int(input ("The date you prefer :"))
    t=int(input ("The time you prefer :"))
    file2.write("The movie :")
    file2.write(m)
    file2.write(" ")
    file2.write("Date: ")
    file2.write(str(d))
    file2.write(" ")
    file2.write("Time:  ")
    file2.write(str(t))
    file2.write("\n")
    file1.close()
    file2.close()
    return ("done......\nnext....")
def pay():
    f=open ("bill.txt",'a')
    n=input ("The mode of payment;(csah on arrival/credit card) :")
    f.write("The payment mode is:")
    f.write(n)
    f.close()
    return("done....")
def status():
    f=open ("bill.txt",'r')
    print(f.read())
    f.close()
    return("successfully booked")
def fresh():
    f=open ("bill.txt",'w')
    f.write("Movie Tickets")
    f.write("\n")
    f.close()
    return ("Ok........ proceed")
   
print("******************************************\n***************welcome*******************\n")
print("1,want to book a fresh ticket")
print("2,choose the Movie, Date&Time")
print("3,choose your seat")
print("4,choose the mode of payment")
print("5,show the booking status")
while (True):
    w=int(input ("enter a number corresponding to the choices shown above :"))
    if(w==1):
        print(fresh())
    elif(w==2):
        print (movie ())
    elif(w==4):
        print(pay())
    elif(w==5):
        print(status ())
    else:
        z=input ("press y to try again")
        if(z=="y"):
            continue
        else:
            break
