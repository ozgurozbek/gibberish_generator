d = list(input(bytearray.fromhex("596f757220737472696e673a20").decode()).upper())
o,n,m,a,a_=d,len(d),int(input(bytearray.fromhex("4c616e6775616765206e756d6265723a20").decode())),list("BCDFGHJKLMNPQRSTVWXYZ"),list("AEIOU")
for i in range(n):
    if d[i] in a:o[i]=a[(i+m)%21]
    if d[i] in a_:o[i]=a_[(i+m)%5]
print(''.join(o))
