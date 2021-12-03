import random

def key_creation():
	p, q = random.randint(2,1000), random.randint(2,1000)

	n = p*q

	phi = (p-1)*(q-1)

	return n, phi

print(key_creation())