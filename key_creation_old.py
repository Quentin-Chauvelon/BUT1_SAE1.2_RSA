import random

def ArePrimes(p, q, PrimeNumbersTable):

	IspPrime, IsqPrime = False, False

	for i in PrimeNumbersTable:
		
		if i == p:
			IspPrime = True
		
		if i == q:
			IsqPrime = True

		if IspPrime and IsqPrime:
			break

	return IspPrime and IsqPrime



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

	while p == q or ArePrimes(p, q, PrimeNumbersTable) == False:
		print(p, q)
		p, q = random.randint(2,1000), random.randint(2,1000)


	n = p*q

	phi = (p-1)*(q-1)



	return p, q, n, phi

print(key_creation())
# u x e + v + phi = 1
# u x e = 1 - v * phi
# u x e = 1[phi]

# u : clé privé
# v : clé publique