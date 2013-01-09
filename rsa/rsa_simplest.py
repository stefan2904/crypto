###########  Set up simple RSA-Environment:

p = 11 # prime
q = 13 # prime

m = 42 # message

###############################################################################

###########  Calculate simple RSA-Environment:

N = p * q
phi = (p-1) * (q-1)
e = 23 # Coprime of phi -> ggt(e, phi) = 1
# TODO: "generate" by iterating down from phi and check for ggt

d = 47 # e * d = 1 mod phi(N) 
# TODO: implement extended euclidean algorithm to find d (and k)
# e * d + k * phi = 1 = ggt(e, phi)

# pubkey: e, N
# privkey: d, N

print "calculated pubkey:"
print " e = ", e, "N = ", N
print "calculated privkey:"
print " d = ", d, "N = ", N

########### Crypt:

c = pow(m, e) % N

print "encrypted message:"
print " c = ", c

###########  Decrypt: 

m2 = pow(c, d) % N

print "decrypted message:"
print " m2 = ", m2

###########  Cracking (calcluating d only knowing e and N, maybe some c): RSAP*

# to calculate d, I need e and phi
# (e is the coprime of phi!)
# phi is Euler's totient function of N -> count the relative primes to N
# => phi = (p-1) * (q-1) where p and q are the two (!) primes
# because N = p*q and phi(p*q) = phi(p) * phi(q) and phi(p) = p-1
# => Integer factorization! :(

