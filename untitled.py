def n_premier(n):

	PrimeNumbersTable = [2]
	NotPrimeNumber = False
	i = 3

	if n >= 3:
		while len(PrimeNumbersTable) < n:
			if i%2 != 0:
				for y in PrimeNumbersTable:
					if i%y == 0: # si i est divisible par un nombre premier
						NotPrimeNumber = True # alors ce n'est pas un nombre premier
			else:
				NotPrimeNumber = True # i est pair et n'est donc pas un nombre premier

			if NotPrimeNumber == False: # si i est un nombre premier
				PrimeNumbersTable.append(i) # ajouter i dans le tableau des nombres premiers
				print(PrimeNumbersTable[len(PrimeNumbersTable) - 1])
			NotPrimeNumber = False
			i += 1
		print(PrimeNumbersTable[len(PrimeNumbersTable)-1])
n_premier(1000000000000)

#1545241 / 1471289