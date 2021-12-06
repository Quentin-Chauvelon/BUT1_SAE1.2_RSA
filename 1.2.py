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
	else:
		return extended_gcd(b,a)

print(extended_gcd(49931,811))
print(extended_gcd(811,49931))

# u0 : i, v0 : j, u1 : u, v1 : v, u2 : y, v2 : z