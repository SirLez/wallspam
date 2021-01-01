import amino
import os
#SirLez
#wallspam
#i see u
os.system("clear")
print("\033[1;36m Amino :  \033[1;34mSirLez \n \n \033[1;36minsta : \033[1;34m SirLe0x \n \n \n")
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		email=input("\033[1;31m\n# ur Email : \033[1;0m")
		password=input("\033[1;31m# ur Password : \033[1;0m")
		client.login(email=email,password=password)
		tst=True
	except:
			tst=False
			print("\n# Verify ur account! \n")
			exx=input("# continue?\033[1;32m y/n : \033[1;0m")
			if exx=='N' or exx=='n' or exx=='no':
					os._exit(1)


os.system("clear")
infoos=input("\033[1;33m# User url : \033[1;0m")
infoo=client.get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]
subclient = amino.SubClient(comId=comId,profile=client.profile)
uid=subclient.get_from_code(infoos).objectId
os.system("clear")
cmn=input("\033[1;33m# Type a comment : \033[1;0m")
os.system("clear")
n=0
k = True
while k is True:
	try:
		subclient.comment(message=cmn,userId=uid)
		n=n+1
		print("\033[1;33m",n,"- ""\033[1;32mdone")
	except:
		pass
