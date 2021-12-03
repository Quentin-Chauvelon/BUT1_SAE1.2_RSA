def list_prime(n):

	if n < 2:
		return "Il n'y a aucun nombres premiers inférieurs ou égaux à " + str(n)

	PrimeNumbersTable = [2] # tableau qui stocke les nombres premiers (2 est de base dedans car comme le programme élimine d'office tous les nombres pairs, 2 ne serait pas inclus dedans)
	i = 3

	if n >= 3:
		while i <= n:

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

	return "Les nombres premiers inférieurs ou égaux à " + str(n) + " sont : " + str(PrimeNumbersTable)

print(list_prime(100))

#1545241 / 1471289