id=[]
name=[]
un=[]
pwd=[]
cpw=[]
#print(len(id))
def Signup():
  li=len(id)
  ln=len(name)
  lun=len(un)
  lp=len(pwd)
  lcp=len(cpw)
  #print(li,ln,lun,lp,lcp)
  id.append(li+1)
  name.append(input("\t Enter Full Name \t"))
  un.append(input("\t Create Username  \t"))
  if('@gmail.com' in un[li]):
    pwd.append(input("\t Enter Password  \t"))
    cpw.append(input("\t Confirm Password  \t"))
  else:
    print("User should contain '@gmail.com'")
  if(pwd[li]==cpw[li]):
    print("\n\t\t Signup Success")
    print()
  else:
    print("\t Password Not Matched\n \t Retry")
    Signup()  
#Signup()

def Login():
  aun=input("\t Enter Username \t")
  apw=input("\t Enter Password \t")
  for i in range(len(id)):
    if(aun==un[i]):
      print("\n\t\t Login Success")
      print("https://www.google.com")
    else:
      print("\n\t\t Invalid Details")
def Admin():
  adl=input("\t Enter Admin Username\t")
  adp=input("\t Enter Admin Password\t")
  if(adl=="admin" and adp=="ajju"):
    print("\n\t\t Admin Login")
    Profiles()
  else:
    print("\n\t\t Inavlid Creadentials")
def Profiles():
  for i in range(len(id)):
    print(id[i],name[i],un[i])

'''SB Volatile DB'''
print("\t SB Voltile DB")

while(True):
  print("1.Login \n2.Signup \n3.Admin")
  ch=int(input("Choose--->"))
  print("\n\n")
  if(ch==1):
    Login()
    print("\n\n")
    #Profiles()
    break
  elif(ch==2):
    Signup()
    print("\n\n")
  elif(ch==3):
    Admin()
    print("\n\n")
  else:
    break
