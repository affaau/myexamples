'''Build in library'''
import hashlib


# list all supporting algorithm functions, as of 2020-May
print(hashlib.algorithms_available)
# {'sha512-224', 'sha3-224', 'sm3', 'sha256', 'sha512-256',
#  'sha224', 'sha384', 'shake128', 'sha3_512', 'blake2s', 'md5',
#  'shake_256', 'blake2s256', 'mdc2', 'shake_128', 'md4', 'sha3_384',
#  'blake2b512', 'sha1', 'sha3_256', 'shake256', 'md5-sha1', 'ripemd160',
#  'sha512', 'sha3_224', 'sha3-256', 'sha3-384', 'sha3-512', 'whirlpool',
#  'blake2b'}


m1 = hashlib.sha1()
m1.update(b'this is a pan')
digest1 = m1.digest()


m2 = hashlib.sha1()
m2.update(b'this is ')
digest2 = m2.digest()

print(digest1==digest2)
# False


# repeatedly update is like concatenation
m2.update(b'a pan')
digest3 = m2.digest()

print(digest1==digest3)
# True
