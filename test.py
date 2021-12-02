import rsa

public, private = rsa.newkeys(512)

pub_k = public.n
pub_e = public.e
k = rsa.key.PublicKey(pub_k, pub_e)


n = private.n
e = private.e
d = private.d
p = private.p
q = private.q
pk = rsa.key.PrivateKey(n, e, d, p, q)
print(private)
print(pk)
