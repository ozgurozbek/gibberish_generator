#coder
def encoder():
  for i in range(n):
    if d[i] in a:o[i]=a[(i+m+(a.index(d[i])))%21]
    if d[i] in a_:o[i]=a_[(i+m+(a_.index(d[i])))%5]
  print(''.join(o))

#decoder
def decoder():
  for i in range(n):
    if d[i] in a:o[i]=a[((a.index(d[i]))-m-i)%21]
    if d[i] in a_:o[i]=a_[((a_.index(d[i]))-m-i)%5]
  print(''.join(o))

#loop
while(1):
  d = list(input(bytearray.fromhex("596f757220737472696e673a20").decode()).upper())
  o,n,m,a,a_=d,len(d),int(input(bytearray.fromhex("4c616e6775616765206e756d6265723a20").decode())),list("BCDFGHJKLMNPQRSTVWXYZ"),list("AEIOU")

  #for you to find out what was that word
  print("1 for decode anything else for encode :> ")
  decoder() if input()=="1" else encoder()
