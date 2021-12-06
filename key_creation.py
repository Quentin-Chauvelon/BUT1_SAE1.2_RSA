import random

def extended_gcd(a,b):

	if a > b:
		u,v,i,j,c,d = 0,1,1,0,a,b

		while 1 :
			q = a//b
			r = a%b

			if r == 0:
				return u, v, (c*u) + (d*v)

			a = b
			b = r

			y = i - q*u
			z = j - q*v
			
			i = u
			j = v

			u = y
			v = z


def encryption(n, priv, msg):

	# if message > n return


def key_creation():

	i = 3
	p, q = 0, 0
	PrimeNumbersTable = [2]

	while i <= 1000:

			PrimeNumber = True

			if i%2 != 0:

				for y in PrimeNumbersTable:
					if i%y == 0: # si i est divisible par un nombre premier
						PrimeNumber = False # alors ce n'est pas un nombre premier
			else:
				PrimeNumber = False # i est pair alors il n'est pas un nombre premier

			if PrimeNumber: # si i est un nombre premier
				PrimeNumbersTable.append(i) # ajouter i dans le tableau des nombres premiers
			
			i += 1

	while p == q: # p et q doivent être différents
		p, q = PrimeNumbersTable[random.randint(0,len(PrimeNumbersTable) - 1)], PrimeNumbersTable[random.randint(0,len(PrimeNumbersTable) - 1)] # prendre un nombre aléatoirement dans la liste des nombres premiers entre 2 et 1000 (revient à faire une boucle jusqu'à avoir deux nombres premiers entre 2 et 1000)


	n = p*q

	phi = (p-1)*(q-1)

	e = 2

	while True:
		_,_,d = extended_gcd(phi, e) # d prend la valeur du pgcd de phi et e
		
		if d == 1: # si le pgcd est de 1 alors on garde le e
			break

		e += 1 # augmenter jusqu'à avoir un e qui fait un pgcd de 1 avec phi


#

	u,v,_ = extended_gcd(phi, e)

	if v >= 0:
		d = v
	else:
		d = -v

	print("Clé publique : (" + str(n) + ", " + str(e) + "), clé privée : (" + str(n) + ", " + str(d) + ")")

	encryption(n, pub, msg)

print(key_creation())