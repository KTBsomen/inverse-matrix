import numpy as np
while True:
	
	
	class adjmatr():
		
		
		
	
		print("\t\t\033[33m.....we support only 3x3 matrix....\033[0m")
		print("\n\033[36m Mod of Your Matrix : 1\033[0m")
		print("\n\033[36m Adjoint of Your Matrix : 2 \033[0m")
		print("\n\033[36m Inverse of Your Matrix : 3 \033[0m")
		print('')
		
		print("\n But First type your 3x3 matrix as bellow : \n")
		
		tfg=np.array(['A','B','C','D','E','F','G','H','I'])
		MAJ=tfg.reshape(3,3)
		print(MAJ)
		
	
		global A
		global B
		global C
		global D
		global E
		global F
		global G
		global H
		global I
			
		A=int(input("\033[32mA :  "))
		B=int(input("B :  "))
		C=int(input("C :  "))
		D=int(input("D :  "))
		E=int(input("E :  "))
		F=int(input("F :  "))
		G=int(input("G :  "))
		H=int(input("H :  "))
		I=int(input("I :  "))
		print("\033[0m")
		
			#AA=int(input("AA :  "))
			#XX=int(input("KK :  "))
		ar=np.array([A,B,C,D,E,F,G,H,I])
		ar1=ar.reshape(3,3)
			
			#print(" your matrix look like : \t")
		print("\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
		print("\033[33mLet ,  your  matrix  be  'A' \033[0m" )
			
		print("  A  =  ")
		print("\n\033[33m",ar1,"\033[0m")
			
		print("")
		
		print("\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
		def modof():
			global mod
			mod=(+(A*((E*I)-(F*H)))-(B*((D*I)-(F*G)))+(C*((D*H)-(G*E))))
			print('')
			print("\033[32m the |A|  = \033[0m","\033[36m",mod,"\033[0m")
			print('')
	
			
			
			
			
		def cofac():
			
			AA=+((E*I)-(F*H))
			BB=-((D*I)-(F*G))
			CC=+((D*H)-(G*E))
			DD=-((B*I)-(C*H))
			EE=+((A*I)-(C*G))
			FF=-((A*H)-(B*G))
			GG=+((B*F)-(C*E))
			HH=-((A*F)-(C*D))
			II=+((A*E)-(B*D))
			arr=np.array([AA,BB,CC,DD,EE,FF,GG,HH,II])
			ar2=arr.reshape(3,3)
			global adjmain
			adjmain=ar2.transpose()
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			#print("\t",mod)
			print('')
			print("\033[35m Let, 'D' is the matrix with the CO-factor of  |A| \033[0m ")
			print("\033[31m D =  \033[0m")
			print('')
			print(ar2)
			print("")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("\033[33mSo the adjoint of your matrix(A) [adjA] :  \033[0m")
			print("\n",adjmain)
			print("\033[33m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
		def ainverse():
			mod=(+(A*((E*I)-(F*H)))-(B*((D*I)-(F*G)))+(C*((D*H)-(G*E))))
			AA=+((E*I)-(F*H))
			BB=-((D*I)-(F*G))
			CC=+((D*H)-(G*E))
			DD=-((B*I)-(C*H))
			EE=+((A*I)-(C*G))
			FF=-((A*H)-(B*G))
			GG=+((B*F)-(C*E))
			HH=-((A*F)-(C*D))
			II=+((A*E)-(B*D))
			arr=np.array([AA,BB,CC,DD,EE,FF,GG,HH,II])
			ar2=arr.reshape(3,3)
			global adjmain
			adjmain=ar2.transpose()
			
			
			
			
			
			
			
			
			
			print(" \033[33mNow the A`¹ {A inverse} =  \n\033[0m")
			gun=(1/mod)*(adjmain)
			print("")
			print("\033[33m\n1/%d"%mod,"x\n",adjmain)
			print("\nor,")
			print(gun)
			print("")
			print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0m")
			#invrs=input("Do you want to multiply any matrix with A`¹ {A inverse}  [y/n] :  ")
		for i in range(0,3):
			
				#
			print("Now Enter Your choice : ")
			first=input("\033[36m choice@\033[0m : ")
			if first=="1":
				modof()
			if first=="2":
				cofac()
			if first=="3":
				ainverse()
			
			#fgh=input("again [y/n]: ")
			#if fgh=="y":
				
				
				